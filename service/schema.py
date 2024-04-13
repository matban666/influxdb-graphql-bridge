import os
import logging
import dotenv
import datetime
import influxdb_client
import graphene
from graphene_django import DjangoObjectType
from common.enums import aggregation
from service import models as service_models
from django.db import models

# from data_access_influx.solar_generation import SolarGeneration

logger = logging.getLogger(__name__)  # Get logger for current module


class InfluxData(models.Model):
    entityId = models.CharField(max_length=100)
    time = models.DateTimeField()
    meanValue = models.FloatField()

class InfluxDataPoint(DjangoObjectType):
    class Meta:
        model = InfluxData

class Query(graphene.ObjectType):
    get_influx_data = graphene.List(
        InfluxDataPoint,
        bucket=graphene.String(default_value="homeassistant"),
        friendly_names=graphene.List(graphene.String, required=True),
        start_time=graphene.DateTime(required=True),
        end_time=graphene.DateTime(required=True),
    )


    @staticmethod
    def convert_to_datetime(value):
        """
        This function checks if a value is a date object and converts it to a datetime object if so.

        Args:
            value: The value to be checked and potentially converted.

        Returns:
            A datetime object if the value is a date, otherwise the original value.
        """

        if isinstance(value, datetime.date):
            # If it's a date object, assume midnight (00:00:00)
            return datetime.datetime.combine(value, datetime.datetime.min.time())
        else:
            # Not a date, return the original value
            return value

    def resolve_get_influx_data(self, info, bucket, friendly_names, start_time, end_time):
        logger.info("resolve_get_influx_data")

        # 1. Construct Flux query with parameters, including the filter based on friendly_names

        # Example Flux query:

        friendly_names_string = (" or ").join([f'r["friendly_name"] == "{name}"' for name in friendly_names])

        query = f'''
          from(bucket: "{bucket}")
          |> range(start: {Query.convert_to_datetime(start_time).strftime("%Y-%m-%dT%H:%M:%SZ")}, stop: {Query.convert_to_datetime(end_time).strftime("%Y-%m-%dT%H:%M:%SZ")})
          |> filter(fn: (r) => r["_measurement"] == "kWh")
          |> filter(fn: (r) => r["_field"] == "value")
          |> filter(fn: (r) => {friendly_names_string})
          |> aggregateWindow(every: 1h, fn: max, createEmpty: true)
          |> difference(nonNegative: true)'''
        
        logger.info(f"resolve_get_influx_data query: {query}")

        # 2. Instantiate InfluxDB Client
        dotenv.load_dotenv()
        client = influxdb_client.InfluxDBClient(
            url=os.environ.get('INFLUXDB_URL'),
            token=os.environ.get('INFLUXDB_TOKEN'),
            org=os.environ.get('INFLUXDB_HOME')
        )

        # 3. Execute Flux query
        query_api = client.query_api()
        result = query_api.query(org=os.environ.get('INFLUXDB_HOME'), query=query)

        logger.info(f"resolve_get_influx_data query result: {result}")

        # 4. Transform InfluxDB results into a list of InfluxDataPoint objects
        influx_data = []
        for record in result:
            for table in record.records:
                value = table.get_value()

                if value is not None:
                    data_point = InfluxDataPoint(
                        entityId=table.values.get('friendly_name'),
                        time=table.get_time(),
                        meanValue=value
                    )
                    if data_point is not None:
                        influx_data.append(data_point)

        return influx_data

schema = graphene.Schema(query=Query)

# influxdb-graphql-bridge
Graph QL server that queries influxdb 

To run:

1. Create a .env file, ensure it is in .gitignore
2. Create and activate python venv from requirements.txt
3. Generate a secret key: python generate_secret_key.py
4. To .env add: SECRET_KEY=<YOUR_SECRET_KEY> (used in settings.py)
3. python manage.py runserver


Operation:

Before GraphQL Query call:
GET http://127.0.0.1:8001/get-csrf-token/


Example Graph QL Query:

Set headers: 
X-CSRFToken: <TOKEN FROM get-csrf-token> 
Cookie: csrftoken=<TOKEN FROM get-csrf-token>

In Postman set POST body to raw Text:

query {
  getInfluxData(
    friendlyNames: ["Home 2 1D", "Grid Export", "Grid Import", "Solar 1 1D"]
    startTime: "2024-04-11T07:00:00Z"
    endTime: "2024-04-12T16:59:59Z"
  ) {
    entityId  # Assuming 'friendly_name' is included in InfluxDataPoint
    time
    meanValue 
  }
}

Example Result:

{
    "getInfluxData": [
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T02:00:00+00:00",
            "meanValue": 0.101
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T03:00:00+00:00",
            "meanValue": 0.09699999999999998
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T04:00:00+00:00",
            "meanValue": 0.10200000000000004
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T05:00:00+00:00",
            "meanValue": 0.122
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T06:00:00+00:00",
            "meanValue": 0.122
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T07:00:00+00:00",
            "meanValue": 0.43499999999999994
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T08:00:00+00:00",
            "meanValue": 0.5840000000000001
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T09:00:00+00:00",
            "meanValue": 0.813
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T10:00:00+00:00",
            "meanValue": 1.572
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T11:00:00+00:00",
            "meanValue": 0.4240000000000004
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T12:00:00+00:00",
            "meanValue": 0.5249999999999995
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T13:00:00+00:00",
            "meanValue": 0.3520000000000003
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T14:00:00+00:00",
            "meanValue": 0.5800000000000001
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T15:00:00+00:00",
            "meanValue": 1.2639999999999993
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T16:00:00+00:00",
            "meanValue": 0.6230000000000002
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T17:00:00+00:00",
            "meanValue": 1.4729999999999999
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T18:00:00+00:00",
            "meanValue": 0.652000000000001
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T19:00:00+00:00",
            "meanValue": 0.2079999999999984
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T20:00:00+00:00",
            "meanValue": 0.2350000000000012
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T21:00:00+00:00",
            "meanValue": 0.1639999999999997
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T22:00:00+00:00",
            "meanValue": 0.2270000000000003
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-11T23:00:00+00:00",
            "meanValue": 0.12100000000000044
        },
        {
            "entityId": "Home 2 1D",
            "time": "2024-04-12T00:00:00+00:00",
            "meanValue": 0.0029999999999983373
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T08:00:00+00:00",
            "meanValue": 0.010000000000000002
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T09:00:00+00:00",
            "meanValue": 0.010000000000000002
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T10:00:00+00:00",
            "meanValue": 0.03
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T11:00:00+00:00",
            "meanValue": 0.16999999999999998
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T12:00:00+00:00",
            "meanValue": 0.010000000000000009
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T13:00:00+00:00",
            "meanValue": 0.27
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T14:00:00+00:00",
            "meanValue": 1.21
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T15:00:00+00:00",
            "meanValue": 1.0000000000000002
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T16:00:00+00:00",
            "meanValue": 0.8899999999999997
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T17:00:00+00:00",
            "meanValue": 0.5099999999999998
        },
        {
            "entityId": "Grid Export",
            "time": "2024-04-11T18:00:00+00:00",
            "meanValue": 0.8700000000000001
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T03:00:00+00:00",
            "meanValue": 0.01
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T04:00:00+00:00",
            "meanValue": 0.009999999999999998
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T06:00:00+00:00",
            "meanValue": 0.010000000000000002
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T07:00:00+00:00",
            "meanValue": 0.049999999999999996
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T08:00:00+00:00",
            "meanValue": 0.03
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T09:00:00+00:00",
            "meanValue": 0.020000000000000018
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T10:00:00+00:00",
            "meanValue": 0.03999999999999998
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T12:00:00+00:00",
            "meanValue": 0.020000000000000018
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T13:00:00+00:00",
            "meanValue": 0.009999999999999981
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T15:00:00+00:00",
            "meanValue": 0.010000000000000009
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T17:00:00+00:00",
            "meanValue": 0.03
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T19:00:00+00:00",
            "meanValue": 0.010000000000000009
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T20:00:00+00:00",
            "meanValue": 0.010000000000000009
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T21:00:00+00:00",
            "meanValue": 0.010000000000000009
        },
        {
            "entityId": "Grid Import",
            "time": "2024-04-11T23:00:00+00:00",
            "meanValue": 0.009999999999999953
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T06:00:00+00:00",
            "meanValue": 0.049999999999999996
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T07:00:00+00:00",
            "meanValue": 0.33
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T08:00:00+00:00",
            "meanValue": 0.533
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T09:00:00+00:00",
            "meanValue": 0.8489999999999999
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T10:00:00+00:00",
            "meanValue": 1.6720000000000002
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T11:00:00+00:00",
            "meanValue": 2.7609999999999997
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T12:00:00+00:00",
            "meanValue": 1.8599999999999994
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T13:00:00+00:00",
            "meanValue": 2.4910000000000014
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T14:00:00+00:00",
            "meanValue": 2.497
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T15:00:00+00:00",
            "meanValue": 2.144
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T16:00:00+00:00",
            "meanValue": 1.450000000000001
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T17:00:00+00:00",
            "meanValue": 0.7109999999999985
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T18:00:00+00:00",
            "meanValue": 0.3979999999999997
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T19:00:00+00:00",
            "meanValue": 0.07400000000000162
        },
        {
            "entityId": "Solar 1 1D",
            "time": "2024-04-11T20:00:00+00:00",
            "meanValue": 0.004999999999999005
        }
    ]
}

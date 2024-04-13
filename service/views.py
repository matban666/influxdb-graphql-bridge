from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
from .schema import schema
import logging

logger = logging.getLogger(__name__)  # Get logger for current module


# Create your views here.
def graphql_view(request):
    """
    View function for handling GraphQL requests.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        JsonResponse: The JSON response containing the result of the GraphQL query.

    """
    if request.method == 'POST':
        data = request.body.decode('utf-8')
        # Parse request data (optional, can use libraries like graphql-core)
        logger.info(f"JsonResponse data: {data}")
        result = schema.execute(data)
        logger.info(f"JsonResponse result: {result}")
        return JsonResponse(result.data, safe=True)
    return JsonResponse({'message': 'Use POST request with GraphQL query'})


def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrfToken': csrf_token})

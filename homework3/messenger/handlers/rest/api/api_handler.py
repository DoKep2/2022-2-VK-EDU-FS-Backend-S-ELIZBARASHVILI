from rest_framework.views import exception_handler


def handler(ex, context):
    response = exception_handler(ex, context)
    if response is not None:
        response.status_code = response.status_code
    return response

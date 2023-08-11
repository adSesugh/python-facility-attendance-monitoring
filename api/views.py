from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response('Hello Facility Monitoring', status=status.HTTP_200_OK)
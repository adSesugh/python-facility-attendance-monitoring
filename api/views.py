from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics, viewsets
from django.contrib.auth import authenticate
from rest_framework.views import APIView


from core.serializers import LaboratorySerializer, UserSerializer, Laboratory

@api_view(['GET'])
def index(request):
    return Response({'message': "Here is Facility Watch App"}, status=status.HTTP_200_OK)

@api_view(['GET'])
def home(request):
    return Response('Hello Facility Monitoring', status=status.HTTP_200_OK)

class LaboratoryViewSet(viewsets.ModelViewSet):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer
    
    def create(self, request, *args, **kwargs):
        laboratory = Laboratory(
            name = request.data.get('name'),
            code = request.data.get('code'),
            created_by = request.user
        )
        
        laboratory.save()
        return laboratory
    
class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
    
class LoginView(APIView):
    permission_classes = ()
    
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)
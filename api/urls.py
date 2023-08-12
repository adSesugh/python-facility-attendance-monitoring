from django.urls import path, include
from rest_framework.routers import DefaultRouter
 
from . import views
from api.views import LaboratoryViewSet, UserCreate

routers = DefaultRouter()
routers.register(r'laboratories', LaboratoryViewSet, basename='laboratories')

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user_create'),
    path('auth/', include('rest_framework.urls')),
]

urlpatterns += routers.urls


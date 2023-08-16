from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
 
from . import views
from api.views import LaboratoryViewSet, UserCreate

routers = DefaultRouter()
routers.register(r'laboratories', LaboratoryViewSet, basename='laboratories')

urlpatterns = [
    path('users/', UserCreate.as_view(), name='user_create'),
    path('auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += routers.urls


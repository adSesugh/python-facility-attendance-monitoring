from django.shortcuts import render
from rest_framework import viewsets
from core.serializers import LaboratorySerializer, Laboratory

class LaboratoryViewSet(viewsets.ModelViewSet):
    queryset = Laboratory.objects.all()
    serializer_class = LaboratorySerializer
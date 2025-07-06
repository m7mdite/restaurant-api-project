from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import MenuItem
from .serializers import MenuItemSerializer
from .filters import MenuItemFilter

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = MenuItemFilter
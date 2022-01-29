from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BootcampSerializer
from .models import Bootcamp
from rest_framework import permissions
from .permissions import IsOwner

# Create your views here.

class BootcampList(ListCreateAPIView):
    serializer_class = BootcampSerializer
    queryset = Bootcamp.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class BootcampDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = BootcampSerializer
    queryset = Bootcamp.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_fields = "id"

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

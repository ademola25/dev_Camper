from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import CoursesSerializer
from .models import Courses
from rest_framework import permissions
from bootcamp.permissions import IsOwner

# Create your views here.

class CoursesList(ListCreateAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

class CoursesDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = CoursesSerializer
    queryset = Courses.objects.all()
    permission_classes = (permissions.IsAuthenticated, IsOwner,)
    lookup_fields = "id"

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

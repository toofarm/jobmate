from django.shortcuts import render
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from .permission import JobPermission


# Create your views here.
class JobViewSet(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [JobPermission]

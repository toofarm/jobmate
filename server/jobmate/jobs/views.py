from django.shortcuts import render
from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [IsOwnerOrReadOnly]

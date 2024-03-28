from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .permissions import UserPermission
from .models import User
from rest_framework.generics import CreateAPIView


# Create your views here.
class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-date_joined")
    permission_classes = [
        UserPermission,
    ]

# class UserCreateView(CreateAPIView):
#     serializer_class = UserSerializer
#     queryset = User.objects.all()
#     permission_classes = [
#         UserPermission,
#     ]

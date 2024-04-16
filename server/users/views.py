from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer
from .permissions import UserPermission
from .models import User
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response


# Create your views here.
class UserViewSet(ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all().order_by("-date_joined")
    permission_classes = [
        UserPermission,
    ] 

class IsAuthenticated(CreateAPIView):
    def get(self, request):
        return Response({"authenticated": request.user.is_authenticated})

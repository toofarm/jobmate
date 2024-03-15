from django.contrib import admin
from django.urls import include, path

from rest_framework.authtoken import routers

from user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("auth/", include("rest_framework.urls", namespace="rest_framework")),
]

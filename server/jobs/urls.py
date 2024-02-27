from django.urls import path
from rest_framework.routers import format_suffix_patterns
from .views import JobViewSet

urlpatterns = [
    path("jobs/", JobViewSet.as_view(), name="job-list"),
    path("jobs/<int:pk>/", JobViewSet.as_view(), name="job-detail"),
]


urlpatterns = format_suffix_patterns(urlpatterns)

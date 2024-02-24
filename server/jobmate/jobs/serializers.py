from rest_framework import serializers
from .models import Job


class JobSerializer(serializers.ModelSerializer):
    applied_formatted = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True
    )
    created_formatted = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M:%S", read_only=True
    )

    class Meta:
        model = Job
        exclude = ["created_by"]  # Exclude 'created_by' field from serialization

from django.db import models
from jobmate import settings
from django.contrib.auth.models import User


class Job(models.Model):

    class Confidence(models.TextChoices):
        HIGH = "High", "High"
        MEDIUM = "Medium", "Medium"
        LOW = "Low", "Low"

    title = models.CharField(max_length=100, blank=False, null=False)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    description = models.TextField()
    link = models.URLField(max_length=200)
    contact = models.CharField(max_length=100, blank=True, null=True)
    applied = models.DateTimeField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    follow_up = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    confidence = models.CharField(
        max_length=10,
        choices=Confidence.choices,
        default=Confidence.HIGH,
    )
    resume = models.FileField(upload_to="static/", blank=True, null=True)
    cover_letter = models.FileField(upload_to="static/", blank=True, null=True)

    def __str__(self):
        return self.title


class Interaction(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.job.title


class Company(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    description = models.TextField()
    website = models.URLField(max_length=200)
    contact = models.CharField(max_length=100, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    logo = models.ImageField(upload_to="static/", blank=True, null=True)

    def __str__(self):
        return self.name

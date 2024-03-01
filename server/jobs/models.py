from django.db import models
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
    applied = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    follow_up = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
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
    date = models.DateTimeField(auto_now_add=True)
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
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    jobs_applied = models.ManyToManyField(Job, blank=True, related_name="jobs_applied")

    def __str__(self):
        return self.name

from django.contrib import admin
from .models import User, Job, Interaction, Company

# Register your models here.
admin.site.register(User)
admin.site.register(Job)
admin.site.register(Interaction)
admin.site.register(Company)

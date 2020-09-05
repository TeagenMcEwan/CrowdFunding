from django.contrib import admin
from .models import Project, Pledge
#Add other fields) above after pledge

# Register your models here.

admin.site.register(Project)
admin.site.register(Pledge)

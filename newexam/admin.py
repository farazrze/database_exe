from django.contrib import admin
from .models import ex
class exed(admin.ModelAdmin):
    ordering = ['name']
    list_display = ['name','sex']



admin.site.register(ex,exed)

from django.contrib import admin

from database.models import *
class datadb(admin.ModelAdmin):
    ordering=['date']

admin.site.register(data,datadb)

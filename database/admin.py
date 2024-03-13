from django.contrib import admin

from database.models import *
class datadb(admin.ModelAdmin):
    ordering=['date']
    list_display = ['id','name','number']

admin.site.register(Data,datadb)

from django.contrib import admin
from testdb.models import *


class editdata(admin.ModelAdmin):
    search_fields=['name']
    list_display=['name','last_name']



admin.site.register(data,editdata)






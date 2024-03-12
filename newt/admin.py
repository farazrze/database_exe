from django.contrib import admin
from newt.models import *

class nwetn(admin.ModelAdmin):
    list_display = ['title','id','date']


admin.site.register(nwt,nwetn)
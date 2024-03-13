from django.urls import path
from .views import *

urlpatterns = [
    path('',newexam,name='nw')
]

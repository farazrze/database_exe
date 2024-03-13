from django.urls import path
from .views import *

urlpatterns = [
    path('',data,name='data'),
    path('<str:name>',test)
]


from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('testdb.urls')),
    path('newt/',include('newt.urls')),
    path('database/',include('database.urls')),
    path('newexam/',include('newexam.urls')),

]

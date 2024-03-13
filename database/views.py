from django.shortcuts import render
from django.http import HttpResponse
from database.models import Data

def data(request):
    return HttpResponse('ascasc')

def test(request):
    data1=Data.objects.all()
    context = {'data1':data1}
    return render (request,'test.html',context)

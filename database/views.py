from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from database.models import Data

def data(request):
    return HttpResponse('ascasc')

def test(request,name):
    data1=get_object_or_404(Data,name=name)
    context = {'data':data1}
    return render (request,'test.html',context)

from django.shortcuts import render
from django.http import HttpResponse

def nt(request):
    return HttpResponse('hello canada')
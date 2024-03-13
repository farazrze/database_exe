from django.shortcuts import render
from django.http import HttpResponse

def newexam(request):
    return HttpResponse('testexam')

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dhoni(request):
    return HttpResponse('Hai this app1 Dhoni')

def rohit(request):
    return HttpResponse('Rohit the Hit Man')
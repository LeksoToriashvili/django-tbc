from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def view1(request):
    return HttpResponse("order view1")


def view2(request):
    return HttpResponse("order view2")

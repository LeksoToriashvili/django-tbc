from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.


def view1(request):
    return HttpResponse("store view1")


def view2(request):
    return HttpResponse("store view2")

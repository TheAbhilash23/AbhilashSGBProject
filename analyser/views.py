from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def mlmodel(request):
    return HttpResponse("Here is your model")


def correlation(request):
    return HttpResponse("Here is correlation heatmap")








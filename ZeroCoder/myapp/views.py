from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def data_view(request):
    return HttpResponse("Это страница Data")


def test_view(request):
    return HttpResponse("Это страница Test")
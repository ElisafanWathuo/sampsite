from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("You are on the polls index")

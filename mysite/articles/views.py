from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    # render(request, )
    return HttpResponse("<h1>Articles!</h1>")

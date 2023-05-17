from django.shortcuts import render
from django.http import HttpResponse

def api_app (request):
    return HttpResponse("<h1>API</h1>")
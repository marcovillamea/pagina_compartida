from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def index(request):
    return render(request, 'index.html')


def not_found(request):
    return render(request,"notfound.html")

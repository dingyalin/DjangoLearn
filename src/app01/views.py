from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def index(request):
    context = {}
    return render(request, 'app01/index.html', context)
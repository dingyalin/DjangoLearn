from django.shortcuts import render
from django.http import HttpRequest

from .models import BBS, BBS_user

# Create your views here.

def index(request):
    bbs_list = BBS.objects.all()
    context = {"bbs_list": bbs_list}
    return render(request, 'app01/index.html', context)

def detail(request, bbs_id):
    bbs = BBS.objects.get(id=bbs_id)
    context = {"bbs_obj": bbs}
    return render(request, 'app01/detail.html', context)

def flappy(request):
    context = {}
    return render(request, 'app01/flappy.html', context)
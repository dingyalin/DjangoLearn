from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template.context import RequestContext

from .models import BBS, BBS_user, Comments

# Create your views here.

def index(request):
    bbs_list = BBS.objects.all()
    context = {"bbs_list": bbs_list}
    return render(request, 'app01/index.html', context)

def detail(request, bbs_id):
    bbs = BBS.objects.get(id=bbs_id)
    comments = Comments.objects.filter(bbs=bbs_id)
    context = {"bbs_obj": bbs, "comments": comments}
    return render(request, 'app01/detail.html', context)

def flappy(request):
    context = {}
    return render(request, 'app01/flappy.html', context)

def sub_comment(request):
    print sub_comment.POST
    return HttpResponseRedirect('/detail/1', context_instance=RequestContext(request))
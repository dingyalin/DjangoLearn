# encoding=utf-8
'''
Created on 2016年11月17日

@author: dWX347607
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list_file, name='index'),
    url(r'^prefix=(.*)$', views.list_file, name='index'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^download/$', views.download, name='download'),
]
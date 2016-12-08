# encoding=utf-8
'''
Created on 2016年11月17日

@author: dWX347607
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)$', views.detail, name='detail'),
    url(r'^flappy$', views.flappy, name='flappy'),
    url(r'^sub_comment/$', views.sub_comment, name='sub_comment'),
]
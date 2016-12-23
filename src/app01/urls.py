# encoding=utf-8
'''
Created on 2016年11月17日

@author: dWX347607
'''
import django.contrib.auth.views as auth_views
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(\d+)/$', views.detail, name='detail'),
    url(r'^flappy/$', views.flappy, name='flappy'),
    url(r'^sub_comment/$', views.sub_comment, name='sub_comment'),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'app01/login.html'}),
    url(r'^acc_login/$', views.acc_login, name='acc_login'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout , name='logout'),
]
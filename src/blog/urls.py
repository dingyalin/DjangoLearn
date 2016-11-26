# encoding=utf-8
'''
Created on 2016年11月3日

@author: dWX347607
'''

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    # 首页调用IndexView

]
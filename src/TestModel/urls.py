# encoding=utf-8
'''
Created on 2016年11月1日

@author: dWX347607
'''

from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    url(r'^([0-9]{4})/$', views.year_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/$', views.month_archive),
    #url(r'^articles/([0-9]{4})/([0-9]{2})/([0-9]+)/$', views.article_detail),
]



urlpatterns = urlpatterns + [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



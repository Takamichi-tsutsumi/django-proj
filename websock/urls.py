# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from websock import views

urlpatterns = patterns(
    '',
    url(r'^subjects/$', views.subject_list, name='subject_list'),
    url(r'^changepoint/$', views.change_point, name='changepoint')
)
# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from simpleboard import views


urlpatterns = patterns(
        '',
        url(r'^boards/$', views.board_list, name='board_list'),
        url(r'^board/new/$', views.board_new, name='board_new'),
        url(r'^board/(?P<board_id>\d+)/$', views.board_show, name='board_show'),
        url(r'^board/(?P<board_id>\d+)/post/new/$', views.post_new, name='post_new'),
)
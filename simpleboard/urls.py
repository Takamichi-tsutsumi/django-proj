# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from simpleboard import views
import django.contrib.auth.views


urlpatterns = patterns(
        '',
        url(r'^$', views.top, name='top'),
        url(r'^boards/$', views.board_list, name='board_list'),
        url(r'^board/new/$', views.board_new, name='board_new'),
        url(r'^board/(?P<board_id>\d+)/$', views.board_show, name='board_show'),
        url(r'^board/(?P<board_id>\d+)/post/new/$', views.post_new, name='post_new'),
        url(r'^users/new/$', views.user_new, name='user_new'),
        url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'simpleboard/user_login.html'}),
        url(r'^logout/$', django.contrib.auth.views.logout, {'template_name': 'simpleboard/user_loggedout.html',}),
        url(r'^favorite/$', views.add_favorite, name='add_favorite'),
)
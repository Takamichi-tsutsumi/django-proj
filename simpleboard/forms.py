# -*- coding: utf-8 -*-
from django.forms import ModelForm
from simpleboard.models import Board, Post


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ('title',)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('comment',)

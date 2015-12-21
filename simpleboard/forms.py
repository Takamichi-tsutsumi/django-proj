# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from simpleboard.models import Board, Post


class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ('title',)


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('comment',)


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', )

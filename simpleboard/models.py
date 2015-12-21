# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField(u'Title', max_length=255)

    def __unicode__(self):
        return unicode(self.title) or u''


class Post(models.Model):
    comment = models.TextField(u'Content')
    board = models.ForeignKey(Board, verbose_name=u'Board', related_name='posts')
    user = models.ForeignKey(User, verbose_name=u'User', related_name='posts')

    def __unicode__(self):
        return unicode(self.comment) or u''


class Favorite(models.Model):
    post = models.ForeignKey(Post, verbose_name='Post', related_name='favorites')
    user = models.ForeignKey(User, verbose_name='User', related_name='favorites')

    def __unicode__(self):
        return unicode(self.post) or u''

    def unq_validation(self):
        if Favorite.objects.filter(post=self.post, user=self.user):
            raise ValidationError
        return True

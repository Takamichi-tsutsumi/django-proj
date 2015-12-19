# -*- coding: utf-8 -*-
from django.db import models


class Board(models.Model):
    title = models.CharField(u'タイトル', max_length=255)

    def __unicode__(self):
        return self.title


class Post(models.Model):
    comment = models.TextField(u'Content')
    board = models.ForeignKey(Board, verbose_name=u'ボード', related_name='posts')

    def __unicode__(self):
        return self.comment

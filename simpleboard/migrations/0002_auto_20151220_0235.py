# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('simpleboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('post', models.ForeignKey(related_name=b'favorites', verbose_name=b'Post', to='simpleboard.Post')),
                ('user', models.ForeignKey(related_name=b'favorites', verbose_name=b'User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.ForeignKey(related_name=b'posts', default=1, verbose_name='User', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='board',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='post',
            name='board',
            field=models.ForeignKey(related_name=b'posts', verbose_name='Board', to='simpleboard.Board'),
        ),
    ]

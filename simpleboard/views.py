# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from simpleboard.models import Board, Post
from simpleboard.forms import BoardForm, PostForm


def board_list(request):
    boards = Board.objects.all().order_by('title')
    board = Board()
    form = BoardForm(instance=board)
    return render_to_response(
        'simpleboard/board_list.html',
        {'boards': boards, 'form': form},
        context_instance=RequestContext(request)
    )


def board_show(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    posts = board.posts.all().order_by('-id')
    post = Post()
    form = PostForm(instance=post)
    return render_to_response(
        'simpleboard/board_show.html',
            {'board': board, 'posts': posts, 'form': form},
        context_instance=RequestContext(request)
    )


def board_new(request):
    board = Board()
    if request.method == 'POST':
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.save()
            return redirect('simpleboard:board_list')
    else:
        form = BoardForm(instance=board)

    return render_to_response(
        'simpleboard/board_new.html',
        dict(form=form),
        context_instance=RequestContext(request)
    )


def post_new(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    post = Post()

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.board_id = board.id
            post.save()
            return redirect('simpleboard:board_show', board_id=board_id)
    else:
        form = PostForm(instance=post)

    return render_to_response(
        'simpleboard/post_new.html',
            {'form': form, 'board': board},
        context_instance=RequestContext(request)
    )




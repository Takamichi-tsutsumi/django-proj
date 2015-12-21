# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from simpleboard.models import Board, Post, Favorite
from simpleboard.forms import BoardForm, PostForm, CustomUserCreationForm
import json


LOGIN_URL = '/simpleboard/login/'

LOGIN_REDIRECT_URL = '/simpleboard/'


def top(request):
    return render_to_response(
        'simpleboard/top.html',
            {},
        context_instance=RequestContext(request)
    )


def user_new(request):
    user = User()
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, instance=user)
        if form.is_valid():
            form.save(commit=True)
            return redirect('simpleboard:board_list')

    return render_to_response(
        'simpleboard/user_new.html',
            {'form': form},
        context_instance=RequestContext(request)
    )


@login_required
def board_list(request):
    boards = Board.objects.all().order_by('title')
    board = Board()
    form = BoardForm(instance=board)
    return render_to_response(
        'simpleboard/board_list.html',
        {'boards': boards, 'form': form},
        context_instance=RequestContext(request)
    )


@login_required
def board_show(request, board_id):
    faved_post_ids = []
    fav_posts = Favorite.objects.filter(user_id=request.user.id).values('post_id',)
    for obj in fav_posts:
        faved_post_ids.append(int(obj['post_id']))
    print faved_post_ids
    board = get_object_or_404(Board, pk=board_id)
    posts = board.posts.all().order_by('-id')
    post = Post()
    form = PostForm(instance=post)
    return render_to_response(
        'simpleboard/board_show.html',
            {'board': board, 'posts': posts, 'form': form, 'faved_id': faved_post_ids},
        context_instance=RequestContext(request)
    )


@login_required
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


@login_required
def post_new(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    post = Post()

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.board_id = board.id
            post.user_id = request.user.id
            post.save()
            return redirect('simpleboard:board_show', board_id=board_id)
    else:
        form = PostForm(instance=post)

    return render_to_response(
        'simpleboard/post_new.html',
            {'form': form, 'board': board},
        context_instance=RequestContext(request)
    )


@login_required
def add_favorite(request):
    from django.http import Http404
    current_user = request.user
    if request.method == 'POST':
        req_data = json.loads(request.body)
        post_id = req_data['post_id']
        fav = Favorite(user_id=current_user.id, post_id=post_id)
        if fav.unq_validation():
            fav.save()
            res = {
                'status': 200,
                'message': 'Successfully favorited!!'
            }
        else:
            res = {
                'status': 302,
                'message': 'You already favs it!'
            }
        return JsonResponse(res)
    else:
        raise Http404


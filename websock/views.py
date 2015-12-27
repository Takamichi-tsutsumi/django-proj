# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from django_socketio import broadcast, broadcast_channel, NoSocket
from django.http import JsonResponse
import json

from websock.models import Subject


def subject_list(request):
    subjects = Subject.objects.all()
    return render_to_response(
        'websock/subject_list.html',
            {'subjects': subjects},
        context_instance=RequestContext(request)
    )


def change_point(request):
    req_data = json.loads(request.body)
    data = {
        "action": "point",
        "sbj-id": req_data['sbj-id'],
        "isLike": req_data['isLike']
    }
    subject = get_object_or_404(Subject, pk=req_data['sbj-id'])
    if req_data['isLike']:
        subject.point += 1
    else:
        subject.point -= 1
    subject.save()
    broadcast(data)
    res = {'status': 200}
    return JsonResponse(res)

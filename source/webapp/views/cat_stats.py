from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from random import random


def cat_view(request: WSGIRequest):
    hapiness = 30
    satiety = 30
    name = request.GET.get('name')
    context = {
        'name': name,
        'age': 1,
        'hapiness': hapiness,
        'satiety': satiety
    }
    if request.POST.get('action') == 'game':
        if random() < 0.3:
            context['hapiness'] == 0
        else:
            context['hapiness'] += 15
            context['satiety'] -= 10
    if request.POST.get('action') == 'feed' and request.POST.get('action') != 'sleep':
        context['hapiness'] += 5
        context['satiety'] += 15
    return render(request, 'cat_stats.html', context=context)
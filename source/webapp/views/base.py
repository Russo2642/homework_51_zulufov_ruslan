from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render
from django.views.generic.base import View
from webapp.models import Name

class IndexView(View):
    def get(self, request: WSGIRequest):
        return render(request, 'index.html')
    
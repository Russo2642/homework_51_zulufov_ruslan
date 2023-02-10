from django.urls import path
from webapp.views.cat_stats import cat_view
from webapp.views.base import IndexView


urlpatterns = [
    path('', IndexView.as_view()),
    path('cat_stats/', cat_view, name = 'cat_stats')
]
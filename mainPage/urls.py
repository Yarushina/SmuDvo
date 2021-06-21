from django.contrib import admin
from django.urls import path
from .views import index
from .views import newsPage
from .views import page_scientists
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', index),
    path('newsPage/<int:news_id>', views.newsPage, name='newsPage'),
    path('PollPage/<int:polls_id>', views.PollPage, name='PollPage'),

    path('adsPage/<int:ads_id>', views.adsPage, name='adsPage'),
    path('page_scientists', page_scientists, name='page_scientists'),
]
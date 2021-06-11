"""
    ask/qa/urls.py
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('login/', views.test, name='test'),
    path('signup/', views.test, name='test'),
    path('question/', views.test, name='test'),
    path('ask/', views.test, name='test'),
    path('popular/', views.test, name='test'),
    path('new/', views.test, name='test'),
]

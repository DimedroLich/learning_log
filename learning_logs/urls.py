"""Схемы URL длы learning logs"""

from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name='index')
]
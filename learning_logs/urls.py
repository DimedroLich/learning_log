"""Схемы URL длы learning logs"""

from django.urls import path
from . import  views

urlpatterns = [
    path('',views.index,name='index'),
    path('topics/',views.topics,name='topics'),
    path('topics/<int:topic_id>/',views.topic,name='topic'),
    path('new_topic/',views.NewTopic.as_view(),name='new_topic'),
    path('new_entry/<int:topic_id>',views.NewEntry.as_view(),name='new_entry'),
    path('edit_entry/<int:entry_id>',views.EditEntry.as_view(),name='edit_entry'),
]
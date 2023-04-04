from django.shortcuts import render
from .models import Topic, Entry


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    context = {
        'topics' : Topic.objects.order_by('date_added'),
    }
    return render(request, 'learning_logs/topics.html', context=context)

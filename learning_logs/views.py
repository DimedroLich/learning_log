from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from .models import Topic, Entry
from .forms import TopicForm, EntryForm


# Create your views here.

def index(request):
    return render(request, 'learning_logs/index.html')


def topics(request):
    context = {
        'topics': Topic.objects.order_by('date_added'),
    }
    return render(request, 'learning_logs/topics.html', context=context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context=context)


class NewTopic(View):
    def get(self, request):
        form = TopicForm()
        context = {
            'form': form
        }
        return render(request, 'learning_logs/new_topic.html', context=context)

    def post(self, request):
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('topics')


class NewEntry(View):

    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        form = EntryForm()
        context = {
            'topic': topic,
            'form': form,
        }
        return render(request, 'learning_logs/new_entry.html', context=context)

    def post(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        form = EntryForm(request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('topic', topic_id=topic_id)


class EditEntry(View):

    def get(self, request, entry_id):
        entry = get_object_or_404(Entry,id=entry_id)
        topic = entry.topic
        form = EntryForm(instance=entry)
        context = {
            "topic" : topic,
            "form" : form,
        }
        return render(request,'learning_logs/new_entry.html',context=context)

    def post(self, request, entry_id):
        entry = get_object_or_404(Entry, id=entry_id)
        topic = entry.topic
        form = EntryForm(request.POST,instance=entry)
        if form.is_valid():
            form.save()
            return redirect('edit_entry',entry_id)

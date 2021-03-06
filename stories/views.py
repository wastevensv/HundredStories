import sys

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.utils import timezone

from .models import Story

# Create your views here.
def index(request):
  recent_story_list = Story.objects.filter(approved=True).order_by('-id')[:100]
  context = RequestContext(request, {
    'recent_story_list': recent_story_list,
  })
  return render(request, 'stories/index.html', context)

def detail(request, story_id):
  story = get_object_or_404(Story, pk=story_id)
  return render(request, 'stories/detail.html', {'story': story})

def write(request):
  return render(request, 'stories/write.html')

def about(request):
  story_count=Story.objects.count()
  return render(request, 'stories/about.html', {'story_count': story_count})

def newstory(request):
  try:
    if not request.POST['title']: title = "Untitled"
    title = request.POST['title']
    story = Story(title=title, text=request.POST['text'], pub_date=timezone.now())
  except Exception as e:
    print(e,file=sys.stderr)
    return HttpResponse("Error Posting Story")
  story.save()
  return redirect('detail', story.id )

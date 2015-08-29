from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Story

# Create your views here.
def index(request):
  recent_story_list = Story.objects.order_by('-pub_date')[:5]
  template = loader.get_template('stories/index.html')
  context = RequestContext(request, {
    'recent_story_list': recent_story_list,
  })
  return HttpResponse(template.render(context))

def detail(request, story_id):
  story = get_object_or_404(Story, pk=story_id)
  return render(request, 'stories/detail.html', {'story': story})

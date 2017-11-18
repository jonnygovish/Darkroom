from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from .models import Photo,Tag

# Create your views here.
def index(request):
  photos = Photo.get_photo()
  tags = Tag.get_tags()
  return render(request,'index.html',{"photos": photos, "tags": tags} )

def photo(request,photo_id):
  try: 
    photo = Photo.objects.get(id = photo_id)
  except DoesNotExist:
    raise Http404()
  return render(request,'photo.html', {"photo": photo})


def tags(request,tag_id):
  try: 
    tag = Tag.objects.get(id = tag_id)
    photos = Photo.objects.filter(tag =tag).all()
  except DoesNotExist:
    raise Http404()
  return render(request,'tag.html', {"tag": tag, "photos":photos})
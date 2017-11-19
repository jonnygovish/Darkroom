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

def search_results(request):

  if 'tag' in request.GET and request.GET['tag']:
    search_term = request.GET.get('tag')
    searched_tags = Tag.search_by_tag(search_term)
    photos = Photo.objects.filter(tag = searched_tags).all()
    message = f"{search_term}"


    return render(request, 'search.html', {"message":message,"tags":searched_tags,"photos":photos})
  else:
    message = "You havent searched for any tag"
    return render(request,'search.html', {"message": message})
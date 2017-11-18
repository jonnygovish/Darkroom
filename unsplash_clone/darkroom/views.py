from django.shortcuts import render
from .models import Photo,Tag

# Create your views here.
def index(request):
  photos = Photo.get_photo()
  tags = Tag.get_tags()
  return render(request,'index.html',{"photos": photos, "tags": tags} )

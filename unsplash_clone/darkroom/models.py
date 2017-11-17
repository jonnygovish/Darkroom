from django.db import models

# Create your models here.

class User(models.Model):
  first_name = models.CharField(max_length = 30)
  last_name = models.CharField(max_length = 30)
  email = models.EmailField()

  def __str__(self):
    return self.first_name

  def save_user(self):
    self.save()

  class Meta:
    ordering = ['first_name']
class Tag(models.Model):
  name = models.CharField(max_length = 30)

  def __str__(self):
    return self.name

class Photo(models.Model):
  photo_image = models.ImageField(upload_to = 'images/')
  pub_date = models. DateTimeField(auto_now_add = True)
  user = models.ForeignKey(User)
  tag = models.ManyToManyField(Tag)
  name = models.CharField(max_length = 30)

  def save_photo(self):
    self.save()

  def delete_photo(self):
    self.Photo.objects.all().delete()

  @classmethod
  def get_photo(cls):
    photos = Photo.objects.all()
    return photos


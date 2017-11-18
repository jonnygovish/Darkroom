from django.contrib import admin
from .models import User,Photo,Tag

# Register your models here.

class PhotoAdmin(admin.ModelAdmin):
  filter_horizontal = ('tag',)

admin.site.register(User)
admin.site.register(Photo,PhotoAdmin)
admin.site.register(Tag)


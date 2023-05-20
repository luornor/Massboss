from django.contrib import admin
from .models import *

# Register your models here.
class MusicAdmin(admin.ModelAdmin):
    list_display = ('title','artist','date')

admin.site.register(Song,MusicAdmin)

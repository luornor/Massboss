from django.db import models
from django.core.validators import FileExtensionValidator


# Create your models here.
class Song(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    producer = models.CharField(max_length=100)
    image = models.ImageField(upload_to='song_images',validators=[FileExtensionValidator(['jpg','png'])])
    song = models.FileField(upload_to='songs',validators=[FileExtensionValidator(['mp3'])])
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.title} by {self.artist}'


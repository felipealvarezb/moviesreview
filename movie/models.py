from email.mime import image
from pickle import TRUE
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100) 
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to = 'media/images')
    url = models.URLField(blank=TRUE)

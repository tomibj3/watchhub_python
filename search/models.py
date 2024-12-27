from django.db import models
from django.conf import settings

# Create your models here.

class SeriesMovie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    genre = models.CharField(max_length=100)
    release_date = models.DateField()
    image = models.ImageField(upload_to='series_movies_project/')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.
class FavNews(models.Model):
    title = models.CharField(max_length=200)
    url = models.TextField()
    thumbnail = models.TextField()
    desc = models.TextField()
    date = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title
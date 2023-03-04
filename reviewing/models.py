from django.db import models


# Create your models here.
class Sportist(models.Model):
    name = models.CharField(max_length=70, null=False)
    age = models.IntegerField(default=(-1))
    sport = models.CharField(max_length=48)
    bio = models.TextField(blank=True, null=True)
    still_playing = models.BooleanField()

    def __str__(self):
        return self.name
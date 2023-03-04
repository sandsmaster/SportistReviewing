from django.db import models

# Create your models here.
class Sportist(models.Model):
    def build(self):
        self.name = models.CharField(max_length=70)
        self.age = models.IntegerField()
        self.sport = models.CharField(max_length=48)
        self.bio = models.TextField()
        self.still_playing = models.BooleanField()
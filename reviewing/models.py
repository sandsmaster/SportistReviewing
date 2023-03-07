from django.db import models


# Create your models here.
class Sportist(models.Model):
    name = models.CharField(max_length=70, null=False)
    age = models.IntegerField(default=(-1))
    sport = models.CharField(max_length=48)
    bio = models.TextField(blank=True, null=True, max_length=255)
    still_playing = models.BooleanField()
    image = models.ImageField(null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Sportist, self).save(*args, **kwargs)


class Contributor(models.Model):
    name = models.CharField(max_length=70, null=False)
    role = models.CharField(max_length=100, null=False)
    image = models.ImageField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True, max_length=100)
    socials = models.TextField(null=True, blank=True, help_text='Social media profiles, on separate lines')
    bio = models.TextField(blank=True, null=True, max_length=921)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(Contributor, self).save(*args, **kwargs)


class Highlights(models.Model):
    title = models.CharField(max_length=300)
    url = models.CharField(null=True, blank=True, max_length=900)
    description = models.TextField(null=True, blank=True, max_length=1200)
    sportist = models.ForeignKey(Sportist, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
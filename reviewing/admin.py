from django.contrib import admin
from .models import Sportist, Contributor, Highlights


# Register your models here.
admin.site.register(Sportist)
admin.site.register(Contributor)
admin.site.register(Highlights)
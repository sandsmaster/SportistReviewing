from django.shortcuts import render
from .models import Sportist


# Create your views here.
def list_sportists(request):

    sportists = Sportist.objects.exclude(sport__isnull=True)

    context = {
        'sps': sportists,
    }

    return render(request, 'sportisti.html', context)
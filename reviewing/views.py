from django.shortcuts import render
from .models import Sportist, Contributor
from django.views.generic import DetailView


# Create your views here.
def list_sportists(request):

    sportists = Sportist.objects.exclude(sport__isnull=True)
    context = {
        'sps': sportists,
    }

    return render(request, 'sportisti.html', context)


def show_about(request):

    contributors = Contributor.objects.exclude(name__isnull=True)
    context = {
        "conts": contributors
    }

    return render(request, 'about.html', context)


class SingleSportistView(DetailView):
    model = Sportist
    template_name = "sportist.html"


class SingleContributorView(DetailView):
    model = Contributor
    template_name = "contributor.html"
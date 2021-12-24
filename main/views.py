from django.shortcuts import render

from .models import Destination


def index(request):
    destinations = Destination.objects.all()
    return render(request, 'main/index.html', {'destinations': destinations})



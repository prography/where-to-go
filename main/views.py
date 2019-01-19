from django.shortcuts import render
from main.models import Landmark, Image

# Create your views here.


def index_page(request):
    return render(request, 'main/index.html', {})


def select_page(request):

    return render(request, 'main/select.html', {})
from django.shortcuts import render
from .models import *


def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/index.html', {'lottos':lottos})
from django.shortcuts import render
from .models import *
from .forms import *


def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/index.html', {'lottos':lottos})

def post(request):
    form = PostForm()
    return render(request, 'lotto/form.html',
                  {'form': form})

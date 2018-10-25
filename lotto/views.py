from django.shortcuts import render, redirect
from .models import *
from .forms import *


def index(request):
    lottos = GuessNumbers.objects.all()
    return render(request, 'lotto/index.html', {'lottos':lottos})

def post(request):
    if request.method == 'GET':
        form = PostForm()
        return render(request, 'lotto/form.html',
                      {'form': form})
    else:  # POST
        form = PostForm(request.POST)
        if form.is_valid():
            lotto = form.save(commit=False)
            lotto.generate()
            return redirect('/lotto')

            # form = PostForm(request.POST)
            # if form.is_valid():
            #     form.save()



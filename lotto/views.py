from django.shortcuts import render, redirect
from .models import *
from .forms import *

# shift + ctrl + -(+) : 숨기기
def index(request):
    lottos = GuessNumbers.objects.all()
    location = Location.objects.get(id=1)
    return render(request, 'lotto/index.html', {'lottos':lottos
                                                ,'location': location})

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

 # 파라미터 방식
def detail(request):
    key = request.GET['lotto_num']
    lotto = GuessNumbers.objects.get(id=key)
    return render(request, 'lotto/detail.html',
                  {'lotto': lotto})
# 다른 방식
def detail2(request, num):
    lotto = GuessNumbers.objects.get(id=num)
    return render(request, 'lotto/detail.html',
                  {'lotto':lotto})

def join(request):
    if request.method == 'GET':
        return render(request, 'lotto/join.html',
                      {})
    else :
        id = request.POST['id']
        pw = request.POST['pw']
        name = request.POST['name']

        # 회원가입 Member 테이블에 데이터 입력
        m = Member(id=id, pw=pw, name=name)
        m.save()

        return render(request,
                      'lotto/join_result.html',
                      {'id':id, 'name':name})
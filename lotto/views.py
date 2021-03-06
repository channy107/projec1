from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

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

def id_check(request):
    id = request.POST['id']
    try:
        Member.objects.get(id=id)
    except Member.DoesNotExist as e:
        pass
        # 가입된 아이디가 없음
        res = {'id': id, 'msg': '가입 가능'}
        return JsonResponse(res)
    else:
        # 가입된 아이디가 있다
        res = {'id': id, 'msg':'가입불가'}
        return JsonResponse(res)
        # return HttpResponse('가입 불가')

def login(request):
    if request.method == 'GET':

        return render(request, 'lotto/login.html', {})
    else:
        id = request.POST['id']
        pw = request.POST['pw']
        try:
            Member.objects.get(id=id, pw=pw)
        except Member.DoesNotExist:
            # 아이디 또는 비밀번호가 틀린경우
            return redirect('login')

        else:
            # 정상 로그인
            # 세션 값 저장 (로그인 시켜주는 것)
            request.session['id'] = id
            return redirect('lotto')

from django.urls import path
from . import views


urlpatterns = [
    # 다른방식
    path('detail/<int:num>',
         views.detail2, name='detail2'),
    # 파라미터 방식
    path('detail', views.detail, name='detail'),
    path('form', views.post),
    path('', views.index),
    path('join', views.join, name='join'),
    path('id_check', views.id_check, name='id_check'),
]
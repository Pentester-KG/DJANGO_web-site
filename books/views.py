from django.shortcuts import render
from django.http import HttpResponse


from datetime import datetime


def info_view(request):
    if request.method == 'GET':
        return HttpResponse('Я Жайлообеков Бексултан, мне 19 лет')


def hobby_view(request):
    if request.method == 'GET':
        return HttpResponse('Создавать подделки')


def current_time_view(request):
    if request.method == 'GET':
        current_time = datetime.now().time()
        return HttpResponse(current_time)

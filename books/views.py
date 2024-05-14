from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AddBooks
from datetime import datetime


def add_books_view(request):
    if request.method == 'GET':
        adds = AddBooks.objects.filter().order_by('-id')
        return render(request, template_name='adds.html', context={'adds': adds})


def add_books_detail_view(request, id):
    if request.method == 'GET':
        added_id = get_object_or_404(AddBooks, id=id)
        return render(request, template_name='added_detail.html',
                      context={'added_id': added_id})


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

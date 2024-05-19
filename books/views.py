from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import AddBooks
from datetime import datetime
from . import forms, models



def add_books_view(request):
    if request.method == 'GET':
        adds = AddBooks.objects.filter().order_by('-id')
        return render(request, template_name='books/adds.html', context={'adds': adds})


def add_books_detail_view(request, id):
    if request.method == 'GET':
        books = get_object_or_404(AddBooks, id=id)
        return render(request, template_name='books/added_detail.html',
                      context={'books': books})


def delete_books_view(request, id):
    book_id = get_object_or_404(AddBooks, id=id)
    book_id.delete()
    return HttpResponse('Книга удалена')

#
# def edit_book_view(request, id):
#     book_id = get_object_or_404(models.AddBooks, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Книга была изменена')
#         else:
#             form = forms.BookForm(instance=book_id)
#         return render(request, template_name='edit_book.html', context={
#             'book_id': book_id,
#             'form': form
#         })


def edit_book_view(request, id):
    book = get_object_or_404(models.AddBooks, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return HttpResponse('Книга была изменена')
    else:
        form = forms.BookForm(instance=book)

    return render(request, 'books/edit_book.html', {'book': book, 'form': form})


def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Ваша книга успешно добавлена</h1>')
    else:
        form = forms.BookForm()

    return render(request, template_name='books/create_books.html', context={'form': form})


def create_comment_view(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Ваш комментарий успешно добавлен</h1>')
    else:
        form = forms.CommentForm()

    return render(request, 'books/create_comment.html', {'form': form})
# def info_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Я Жайлообеков Бексултан, мне 19 лет')
#
#
# def hobby_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Создавать подделки')
#
#
# def current_time_view(request):
#     if request.method == 'GET':
#         current_time = datetime.now().time()
#         return HttpResponse(current_time)

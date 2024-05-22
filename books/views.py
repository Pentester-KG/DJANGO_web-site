from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from . import forms, models


class BooksListView(generic.ListView):
    template_name = "books/adds.html"
    context_object_name = "adds"
    model = models.AddBooks

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class BookDetailView(generic.DetailView):
    template_name = "books/added_detail.html"
    context_object_name = "books"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.AddBooks, id=book_id)


class CreateBookView(generic.CreateView):
    template_name = "books/create_books.html"
    form_class = forms.BookForm
    success_url = '/books/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


class DeleteBookView(generic.DeleteView):
    template_name = "books/delete_book.html"
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.AddBooks, id=book_id)


class EditBookView(generic.UpdateView):
    template_name = "books/edit_book.html"
    form_class = forms.BookForm
    success_url = '/books/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.AddBooks, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBookView, self).form_valid(form=form)


class SearchBookView(generic.ListView):
    template_name = "books/adds.html"
    context_object_name = "adds"
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return models.AddBooks.filter(title__icontains=query).order_by('title')
        return models.AddBooks.objects.all().order_by('title')
    # def get_queryset(self):
    #     return models.AddBooks.objects.filter(title__icontains=self.request.GET.get('q'))
    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['q'] = self.request.GET.get('q')
    #     return context


def create_comment_view(request):
    if request.method == 'POST':
        form = forms.CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Ваш комментарий успешно добавлен</h1>')
    else:
        form = forms.CommentForm()

    return render(request, 'books/create_comment.html', {'form': form})
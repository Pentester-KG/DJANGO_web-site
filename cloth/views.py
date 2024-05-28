from django.shortcuts import render
from . import models
from django.views import generic


class Clothes(generic.ListView):
    template_name = 'cloth/all_clothes.html'
    context_object_name = 'clothes'
    model = models.Cloth

    def get_queryset(self):
        return self.model.objects.filter().order_by('-id')


class MenCloth(generic.ListView):
    template_name = 'cloth/mans_cloth.html'
    context_object_name = 'mans_clothes'
    model = models.Cloth

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='Мужская одежда').order_by('-id')


class WomenCloth(generic.ListView):
    template_name = 'cloth/women_cloth.html'
    context_object_name = 'women_clothes'

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='Женская одежда').order_by('-id')


class ChildCloth(generic.ListView):
    template_name = 'cloth/child_cloth.html'
    context_object_name = 'children_clothes'

    def get_queryset(self):
        return models.Cloth.objects.filter(tags__name='Детская одежда').order_by('-id')

# class CreateClothView(generic.CreateView):
#     template_name = "books/create_books.html"
#     form_class = form
#     success_url = '/books/'
#
#     def form_valid(self, form):
#         print(form.cleaned_data)
#         return super(CreateBookView, self).form_valid(form=form)

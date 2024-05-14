from django.shortcuts import render
from . import models


def all_clothes(request):
    if request.method == 'GET':
        clothes = models.Cloth.objects.filter().order_by('-id')
        return render(request, template_name='cloth/all_clothes.html', context={'clothes': clothes})


def mans_cloth(request):
    if request.method == 'GET':
        mans_clothes = models.Cloth.objects.filter(tags__name='Мужская одежда').order_by('-id')
        return render(request, template_name='cloth/mans_cloth.html', context={'mans_clothes': mans_clothes})


def women_cloth(request):
    if request.method == 'GET':
        women_clothes = models.Cloth.objects.filter(tags__name='Женская одежда').order_by('-id')
        return render(request, template_name='cloth/women_cloth.html', context={'women_clothes': women_clothes})


def child_cloth(request):
    if request.method == 'GET':
        children_clothes = models.Cloth.objects.filter(tags__name='Детская одежда').order_by('-id')
        return render(request, template_name='cloth/child_cloth.html', context={'children_clothes': children_clothes})
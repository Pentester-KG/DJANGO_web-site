from django.urls import path
from . import views

urlpatterns = [
    path('clothes/', views.all_clothes, name='all_clothes'),
    path('mans_cloth/', views.mans_cloth, name='mans_cloth'),
    path('women_cloth/', views.women_cloth, name='women_cloth'),
    path('child_cloth/', views.child_cloth, name='child_cloth'),
]
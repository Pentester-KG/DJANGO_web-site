from django.urls import path
from . import views

urlpatterns = [
    path("", views.Clothes.as_view(), name="all_clothes"),
    path("mans_cloth/", views.MenCloth.as_view(), name="mans_cloth"),
    path("women_cloth/", views.WomenCloth.as_view(), name="women_cloth"),
    path("child_cloth/", views.ChildCloth.as_view(), name="child_cloth"),
]

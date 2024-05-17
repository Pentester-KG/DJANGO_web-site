from django.urls import path
from .views import add_books_view, add_books_detail_view


urlpatterns = [
    path('', add_books_view, name='books'),
    path('<int:id>/', add_books_detail_view, name='books_detail'),
]
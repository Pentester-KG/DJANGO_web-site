from django.urls import path
# from .views import add_books_view, add_books_detail_view, create_book_view
from . import views

urlpatterns = [
    path('', views.add_books_view, name='books'),
    path('books/<int:id>/', views.add_books_detail_view, name='books_detail'),
    path('books/<int:id>/delete/', views.delete_books_view, name='delete_book'),
    path('books/<int:id>/update/', views.edit_book_view, name='edit_book'),
    path('books/<int:id>//', views.edit_book_view, name='edit_book'),
    path('create_book/', views.create_book_view, name='create_book'),
    path('create_comment/', views.create_comment_view, name='create_comm'),

]
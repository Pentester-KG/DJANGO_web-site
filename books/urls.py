from django.urls import path

# from .views import add_books_view, add_books_detail_view, create_book_view
from . import views

urlpatterns = [
    path("books/", views.BooksListView.as_view(), name="books"),
    path("books/<int:id>/", views.BookDetailView.as_view(), name="books_detail"),
    path("books/<int:id>/delete/", views.DeleteBookView.as_view(), name="delete_book"),
    path("books/<int:id>/update/", views.EditBookView.as_view(), name="edit_book"),
    path("create_book/", views.CreateBookView.as_view(), name="create_book"),
    path("create_comment/", views.create_comment_view, name="create_comm"),
    path("search/", views.SearchBookView.as_view(), name="search"),
]

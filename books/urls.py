from django.urls import path
from .views import info_view, hobby_view, current_time_view, add_books_view, add_books_detail_view


urlpatterns = [
    path('info/', info_view, name="info"),
    path('hobby/', hobby_view, name='hobby'),
    path('time/', current_time_view, name='time'),
    path('books/', add_books_view, name='books'),
    path('books/<int:id>/', add_books_detail_view, name='books_detail')
]
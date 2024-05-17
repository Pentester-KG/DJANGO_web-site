from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class AddBooks(models.Model):
    BOOK_GENRE = (
        ('Фантастика', 'Фантастика'),
        ('Детские', 'Детские'),
        ('Хоррор', 'Хоррор'),
        ('Романтика', 'Романтика'),
        ('Детектив', 'Детектив'),
        ('Другое', 'Другое')
    )
    title = models.CharField(max_length=100, verbose_name='Укажите название книги')
    author = models.CharField(max_length=100, verbose_name='Введите автора')
    image = models.ImageField(upload_to='images/', verbose_name='Загрузите фото', null=True)
    description = models.TextField(verbose_name='Напишите описание книги')
    audio_book = models.FileField(upload_to='audio_book/', blank=True, verbose_name='Загрузите аудиокнигу', null=True)
    video = models.URLField(verbose_name='Укажите видео ссылку', blank=True, null=True)
    book_genre = models.CharField(max_length=100, choices=BOOK_GENRE, verbose_name='Выберите жанр')
    price = models.PositiveIntegerField(verbose_name='Укажите цену')
    publication = models.DateTimeField(auto_now_add=True)
    key_words = models.CharField(max_length=100, verbose_name='Ключевые слова')

    def __str__(self):
        return f'{self.title} - {self.publication}'
    class Meta:
        verbose_name = 'книги'
        verbose_name_plural = 'Список книг'


class Review(models.Model):
    review_book = models.ForeignKey(AddBooks, on_delete=models.CASCADE, related_name='review_book', null=True)
    stars = models.PositiveIntegerField(default=5, validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.review_book} - {self.stars}'

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'отзывы'

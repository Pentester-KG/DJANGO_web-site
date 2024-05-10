from django.db import models


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
        verbose_name = 'книгу'
        verbose_name_plural = 'Список книг'

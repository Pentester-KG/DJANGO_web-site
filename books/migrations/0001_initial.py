# Generated by Django 5.0.4 on 2024-05-28 10:50

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AddBooks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "title",
                    models.CharField(
                        max_length=100, verbose_name="Укажите название книги"
                    ),
                ),
                (
                    "author",
                    models.CharField(max_length=100, verbose_name="Введите автора"),
                ),
                (
                    "image",
                    models.ImageField(
                        null=True,
                        upload_to="media/images/",
                        verbose_name="Загрузите фото",
                    ),
                ),
                (
                    "description",
                    models.TextField(verbose_name="Напишите описание книги"),
                ),
                (
                    "audio_book",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="audio_book/",
                        verbose_name="Загрузите аудиокнигу",
                    ),
                ),
                (
                    "video",
                    models.URLField(
                        blank=True, null=True, verbose_name="Укажите видео ссылку"
                    ),
                ),
                (
                    "book_genre",
                    models.CharField(
                        choices=[
                            ("Фантастика", "Фантастика"),
                            ("Детские", "Детские"),
                            ("Хоррор", "Хоррор"),
                            ("Романтика", "Романтика"),
                            ("Детектив", "Детектив"),
                            ("Другое", "Другое"),
                        ],
                        max_length=100,
                        verbose_name="Выберите жанр",
                    ),
                ),
                ("price", models.PositiveIntegerField(verbose_name="Укажите цену")),
                ("publication", models.DateTimeField(auto_now_add=True)),
                (
                    "key_words",
                    models.CharField(max_length=100, verbose_name="Ключевые слова"),
                ),
            ],
            options={
                "verbose_name": "книги",
                "verbose_name_plural": "Список книг",
            },
        ),
        migrations.CreateModel(
            name="Comment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "stars",
                    models.PositiveIntegerField(
                        default=5,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(5),
                        ],
                    ),
                ),
                ("text", models.TextField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "review_book",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="review_book",
                        to="books.addbooks",
                    ),
                ),
            ],
            options={
                "verbose_name": "отзыв",
                "verbose_name_plural": "отзывы",
            },
        ),
    ]

from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(User):
    GENDER = (
        ('Мужской', 'Мужской'),
        ('Женский', 'Женский'),
    )
    MARRIED_STATUS = (
        ('Женат(а)', 'Женат(а)'),
        ('Не женат(а)', 'Не женат(а)')
    )
    age = models.PositiveSmallIntegerField(default=18, validators=[MinValueValidator(16), MaxValueValidator(60)])
    phone_number = models.CharField(max_length=14, default="+996")
    birth_date = models.DateField(verbose_name="Дата рождения")
    gender = models.CharField(max_length=64, choices=GENDER)
    exp_work = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(25)])
    experience_work = models.CharField(max_length=100, default="Стаж не определен")
    married_status = models.CharField(choices=MARRIED_STATUS, default="Не женат/Не замужем", max_length=100)
    education = models.BooleanField(default=False)
    habits = models.CharField(max_length=200, default=None)
    email1 = models.EmailField(max_length=100)


#exp = опыт работы , указывается в годах
@receiver(post_save, sender=UserProfile)
def set_experience(sender, instance, created, **kwargs):
    if created:
        print('Сигнал обработан пользователь создан')
    exp = instance.exp
    if exp <= 1:
        instance.experience_work = 'Junior'
    elif 1 <= exp <= 3:
        instance.experience_work = 'Middle'
    elif 3 <= exp <= 25:
        instance.experience_work = 'Senior'
    else:
        instance.experience_work = "Стаж не определен"
    instance.save()










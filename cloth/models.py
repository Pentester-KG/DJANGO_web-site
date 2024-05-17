from django.db import models


class TagCloth(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Cloth(models.Model):
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='media/cloth', null=True, blank=True)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=100)
    tags = models.ManyToManyField(TagCloth)

    def __str__(self):
        return self.name


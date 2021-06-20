from django.db import models

# Create your models here.


class Pet(models.Model):
    CAT = 'cat'
    DOG = 'dog'
    RODENT = 'rodent'
    KIND_CHOICES = [(CAT, 'cat'),(DOG, 'dog'), (RODENT, 'rodent')]
    name = models.CharField(max_length=100, verbose_name="Кличка")
    kind = models.CharField(max_length=100, choices= KIND_CHOICES, verbose_name="Вид")
    breed = models.CharField(max_length=100, verbose_name="Порода")
    photo = models.ImageField(upload_to='pets_photo', height_field='photo_height', width_field='photo_width', blank=True)
    photo_height = models.PositiveIntegerField()
    photo_width = models.PositiveIntegerField()
    description = models.TextField()
    age = models.IntegerField(verbose_name="Возраст")

    def __str__(self):
        return self.name

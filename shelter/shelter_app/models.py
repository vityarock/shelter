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
    photo = models.ImageField(upload_to='pets_photo', blank=True)
    description = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
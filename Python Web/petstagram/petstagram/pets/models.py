from django.db import models


# Create your models here.
class Pet(models.Model):
    TYPE_CHOICE_DOG = 'dog'
    TYPE_CHOICE_CAT = 'cat'
    TYPE_CHOICE_PARROT = 'parrot'

    TYPE_CHOICES = [
        [TYPE_CHOICE_DOG, 'Dog'],
        [TYPE_CHOICE_CAT, 'Cat'],
        [TYPE_CHOICE_PARROT, 'Parrot'],
    ]

    type = models.CharField(
        max_length=6,
        choices=TYPE_CHOICES,
    )
    name = models.CharField(max_length=6)
    age = models.PositiveIntegerField()
    description = models.TextField()
    image = models.URLField()


class Like(models.Model):
    pet_to_like = models.ForeignKey(Pet, on_delete=models.CASCADE)

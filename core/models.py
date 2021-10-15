from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(
        to = User, on_delete=models.CASCADE,
        related_name='profile'
    )

    region = models.CharField(max_length=1, choices = (
        ('B','Bishkek'),
        ('C', 'Chuy'),
        ('N', 'Naryn'),
        ('I', 'Issyk-kol'),
        ('T', 'Talas'),
        ('J', 'Jalal-abad'),
        ('D', 'Batken'),
    ))

    photo = models.ImageField(
        upload_to = 'profile',
        null = True, blank=True
    )

    def __str__(self):
        return self.user.username
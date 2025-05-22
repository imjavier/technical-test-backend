from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class UserType(models.TextChoices):
        ADMIN = 'admin', 'Administrador'
        EXTERNAL = 'external', 'Externo'

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.EXTERNAL,
        verbose_name='Tipo de usuario'
    )

    class Meta:
        verbose_name = 'usuario'
        verbose_name_plural = 'usuarios'
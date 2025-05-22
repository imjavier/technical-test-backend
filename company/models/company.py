from django.db import models

class Company(models.Model):
    nit = models.CharField(max_length=20, primary_key=True, verbose_name='NIT')
    name = models.CharField(max_length=100, verbose_name='nombre de la empresa')
    address = models.TextField(verbose_name='dirección de la empresa')
    phone = models.CharField(max_length=20, verbose_name='telefono de la empresa')

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'



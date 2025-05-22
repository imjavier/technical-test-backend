from calendar import c
from django.db import models
from company.models.company import Company

class Product(models.Model):
    code = models.CharField(max_length=50, unique=True, verbose_name='codigo')
    name = models.CharField(max_length=100, verbose_name='nombre del producto')
    features = models.TextField(verbose_name='caracteristicas')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, verbose_name='empresa', related_name='products')

    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'


class ProductPrice(models.Model):
    class CurrencyChoices(models.TextChoices):
        COP = 'COP', 'Pesos Colombianos'
        USD = 'USD', 'Dólares'
        EUR = 'EUR', 'Euros'

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='prices', verbose_name='producto')
    currency = models.CharField(
        max_length=3,
        choices=CurrencyChoices.choices,
        default=CurrencyChoices.COP,
        verbose_name='moneda'
    )
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='precio')

    class Meta:
        verbose_name = 'precio del producto'
        verbose_name_plural = 'precios de los productos'

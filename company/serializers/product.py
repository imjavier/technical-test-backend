from rest_framework import serializers
from company.models import Product, ProductPrice

class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    prices = ProductPriceSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
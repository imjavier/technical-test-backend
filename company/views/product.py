from rest_framework import viewsets
from company.models.product import Product, ProductPrice
from company.serializers.product import ProductSerializer, ProductPriceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminUserType
from rest_framework.exceptions import NotFound

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated, IsAdminUserType]
    authentication_classes = [JWTAuthentication]

class ProductPriceViewSet(viewsets.ModelViewSet):
    serializer_class = ProductPriceSerializer
    permission_classes = [IsAuthenticated, IsAdminUserType]
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        product_pk = self.kwargs.get('product_pk')

        if not Product.objects.filter(pk=product_pk).exists():
            raise NotFound('El producto no existe.')

        return ProductPrice.objects.filter(product_id=product_pk)
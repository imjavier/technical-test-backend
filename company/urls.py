from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter
from company.views.company import CompanyViewSet
from company.views.product import ProductViewSet, ProductPriceViewSet

router = DefaultRouter()
router.register(r'companies', CompanyViewSet)
router.register(r'products', ProductViewSet)

product_router = NestedDefaultRouter(router, r'products', lookup='product')
product_router.register(r'prices', ProductPriceViewSet, basename='product-prices')

 
urlpatterns = [
    path('', include(router.urls)),
    path('', include(product_router.urls)),
]
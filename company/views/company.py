from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from company.models.company import Company
from company.serializers import CompanySerializer
from users.permissions import IsAdminOrReadOnly

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsAuthenticated, IsAdminOrReadOnly]

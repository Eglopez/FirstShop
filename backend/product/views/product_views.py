from django.shortcuts import render
from ..serializers import UserSerializer
from ..models import Product

class ProductView(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = Product.objects.all()
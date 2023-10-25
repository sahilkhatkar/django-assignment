from django.shortcuts import render
from rest_framework import viewsets, generics
from home.models import Product
from home.serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

def index(req):
    return render(req, 'index.html')
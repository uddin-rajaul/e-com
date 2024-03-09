from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Brand, Category, Product, ProductLine
from .serializers import BrandSerializer, CategorySerializer, ProductSerializer

# Create your views here.

class CategoryViewSet(viewsets.ViewSet):
    """
        A simple Viewset for viewing all Categories
    """

    queryset = Category.objects.all()

    @extend_schema(responses=CategorySerializer)
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """ 
        Viewset for Brands
    """
    queryset = Brand.objects.all()

    @extend_schema(responses=BrandSerializer)
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ViewSet):
    """ 
        A Viewset for Product
    """
    queryset = Product.objects.all()
    lookup_field = "slug"

    def retrieve(self, request, slug=None):
        serializer = ProductSerializer(self.queryset.filter(slug=slug), many=True)
        return Response(serializer.data)

    @extend_schema(responses=ProductSerializer)
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)
    
    @action(
            methods=["get"], 
            detail=False, 
            url_path=r"category/(?P<category>\w+)/all",
    )
    def list_product_by_category(self, request, category=None):
        """ 
            An endpoint to return product by category
        """
        serializer = ProductSerializer(self.queryset.filter(category__name=category), many=True)
        return Response(serializer.data)
    
    
    

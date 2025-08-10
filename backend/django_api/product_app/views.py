from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from drf_spectacular.utils import extend_schema


from .serializers import ProductSerializer, CategorySerializer, BrandSerializer
from .models import Product, Category, Brand


# Create your views here.
class CategoryViewSet(viewsets.ViewSet):
    """ViewSet for handling category related operations."""

    queryset = Category.objects.all()

    @extend_schema(
        summary="List all categories",
        responses={200: CategorySerializer(many=True)},
    )
    def list(self, request):
        serializer = CategorySerializer(self.queryset, many=True)
        return Response(serializer.data)


class BrandViewSet(viewsets.ViewSet):
    """ViewSet for handling Brand related operations."""

    queryset = Brand.objects.all()

    @extend_schema(
        summary="List all brands",
        responses={200: BrandSerializer(many=True)},
    )
    def list(self, request):
        serializer = BrandSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ProductViewSet(viewsets.ViewSet):
    """ViewSet for handling Product related operations."""

    queryset = Product.objects.all()
    lookup_field = "slug"

    @extend_schema(
        summary="List all products",
        responses={200: ProductSerializer(many=True)},
    )
    def list(self, request):
        serializer = ProductSerializer(self.queryset, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=["get"], url_path="category/(?P<category>[^/.]+)")
    def list_product_by_category(self, request, category=None):
        """List products by category."""
        serializer = ProductSerializer(
            self.queryset.filter(category__name=category), many=True
        )
        return Response(serializer.data)

    def retrieve(self, request, slug=None):
        """Retrieve a single product by its ID."""
        try:
            product = self.queryset.get(slug=slug)
            serializer = ProductSerializer(product)
            return Response(serializer.data)
        except Product.DoesNotExist:
            return Response({"error": "Product not found"}, status=404)

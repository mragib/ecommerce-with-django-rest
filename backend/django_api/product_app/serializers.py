from rest_framework import serializers
from .models import Product, Category, Brand, ProductLine, ProductImage


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        exclude = ("id",)


class ProductLineSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(
        many=True,
    )

    class Meta:
        model = ProductLine
        exclude = ("id", "product", "order", "is_active")


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    product_line = ProductLineSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = "__all__"

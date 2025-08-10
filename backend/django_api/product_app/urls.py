from django.urls import path, include
from .views import CategoryViewSet, BrandViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r"category", CategoryViewSet, basename="category")
router.register(r"brand", BrandViewSet, basename="brand")
router.register(r"list", ProductViewSet, basename="products")
urlpatterns = [
    path("", include(router.urls)),
]

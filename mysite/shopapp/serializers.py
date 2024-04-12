from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Product, Order


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            "pk",
            "name",
            "description",
            "price",
            "discount",
            "created_at",
            "archived",
            "preview",
        )


class OrderSerializer(serializers.ModelSerializer):
    products = ProductSerializer(source="orders", many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "pk",
            "delivery_address",
            "promocode",
            "products",
            "created_at",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
        )

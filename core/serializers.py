from rest_framework import serializers

from .models import (
    Company,
    User,
    Category,
    Product,
)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'name', 'website', 'description', 'is_active',)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'phone',)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.StringRelatedField(
        many=False,
        source='category',
        read_only=True,
        label='Категория',
    )

    company_name = serializers.StringRelatedField(
        many=False,
        source='company',
        read_only=True,
        label='Компания',
    )

    class Meta:
        model = Product
        fields = (
            'id', 'company', 'company_name', 'category', 'category_name', 'name', 'price', 'description', 'is_active',
        )

from django.contrib import admin

from .models import (
    Company,
    User,
    Category,
    Product,
)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'website', 'description', 'is_active',)
    list_filter = ('name', 'is_active',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'phone',)
    list_filter = ('username', 'last_name', 'email', 'phone',)

    def full_name(self, obj):
        full_name = f'{obj.last_name} {obj.first_name} {obj.middle_name}'
        return full_name.strip()


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('company', 'category', 'name', 'price', 'description', 'is_active',)
    list_filter = ('company', 'category', 'name', 'price', 'is_active',)

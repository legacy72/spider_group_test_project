from django.db import models
from django.core.validators import URLValidator
from django.contrib.auth.models import AbstractUser

from phone_field import PhoneField


class Company(models.Model):
    """
    NOTE: постарался не перенасыщать модели множеством полей, так как лучше заполнять поля по мере необходимости (по ТЗ)
    """
    name = models.CharField(
        verbose_name='Название компании',
        max_length=255,
    )

    website = models.URLField(
        verbose_name='Сайт',
        max_length=255,
        validators=[URLValidator()],
        blank=True,
        null=True,
    )

    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        verbose_name='Действителен',
        default=True,
    )

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'
        ordering = ['-id']

    def __str__(self):
        return self.name


class User(AbstractUser):
    username = models.CharField(
        verbose_name='Логин',
        max_length=150,
        unique=True,
    )

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=150,
    )

    last_name = models.CharField(
        verbose_name='Фамилия',
        max_length=150,
    )

    middle_name = models.CharField(
        verbose_name='Отчество',
        max_length=150,
        blank=True,
        null=True,
    )

    email = models.EmailField(
        verbose_name='Email',
        unique=True,
    )

    phone = PhoneField(
        verbose_name='Телефон',
        help_text='Введите номер телефона',
        unique=True,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-id']

    def full_name(self):
        full_name = f'{self.last_name} {self.first_name} {self.middle_name}'
        return full_name.strip()

    def __str__(self):
        return self.full_name()


class Category(models.Model):
    name = models.CharField(
        verbose_name='Название категории',
        max_length=255,
    )

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['-id']

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория',
        related_name='product_category',
    )

    company = models.ForeignKey(
        Company,
        on_delete=models.CASCADE,
        verbose_name='Компания',
        null=True,
        blank=True,
        related_name='product_company',
    )


    name = models.CharField(
        verbose_name='Название категории',
        max_length=255,
    )

    price = models.DecimalField(
        verbose_name='Цена',
        max_digits=30,
        decimal_places=2,
    )

    description = models.TextField(
        verbose_name='Описание',
        null=True,
        blank=True,
    )

    is_active = models.BooleanField(
        verbose_name='Действителен',
        default=True,
    )

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['-id']

    def __str__(self):
        return self.name

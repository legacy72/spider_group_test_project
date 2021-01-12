from rest_framework import viewsets
from rest_framework import filters, status
from rest_framework.decorators import api_view
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response

from .models import (
    Company,
    User,
    Category,
    Product,
)
from .serializers import (
    CompanySerializer,
    UserSerializer,
    CategorySerializer,
    ProductSerializer,
)


@api_view(['POST'])
@permission_classes([AllowAny])
def registration_view(request):
    """
    Вьюшка для создания пользователя

    :param request: email - почта
    :param request: password - пароль
    :param request: repeat_password - повторный пароль для подтверждения
    :return: {
        "email": почта созданного пользователя
    }
    """
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = User.objects.filter(email=serializer.data['email'])
            if user:
                return Response(
                    {'Error': 'Пользователь с таким email уже существует'},
                    status=status.HTTP_409_CONFLICT
                )
            serializer.save()
            data = serializer.data
        else:
            data = serializer.errors
        return Response(data)


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filter_fields = ('id', 'name', 'is_active')
    queryset = Company.objects.filter(is_active=True)

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny(), ]
        return super(CompanyViewSet, self).get_permissions()


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filter_fields = ('id', 'username', 'first_name', 'last_name', 'middle_name', 'email', 'phone',)
    queryset = User.objects.all()


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filter_fields = ('id', 'name',)
    queryset = Category.objects.all()

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny(), ]
        return super(CategoryViewSet, self).get_permissions()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filter_fields = ('id', 'category', 'company', 'name', 'price',)

    def get_queryset(self):
        filtered_name = self.request.query_params.get('filtered_name', '')
        queryset = Product.objects\
            .select_related('category', 'company')\
            .filter(is_active=True, name__icontains=filtered_name)
        return queryset

    def get_permissions(self):
        if self.action == 'list':
            return [AllowAny(), ]
        return super(ProductViewSet, self).get_permissions()

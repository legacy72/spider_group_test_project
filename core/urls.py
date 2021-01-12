from rest_framework import routers

from .views import (
    CompanyViewSet,
    UserViewSet,
    CategoryViewSet,
    ProductViewSet,
)


router = routers.DefaultRouter()

router.register('companies', CompanyViewSet)
router.register('users', UserViewSet)
router.register('categories', CategoryViewSet)
router.register('products', ProductViewSet, basename='products')

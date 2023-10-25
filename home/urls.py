from django.contrib import admin
from home.views import index
from django.urls import path, include
from home.views import ProductViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
# router.register(r'', ProductViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('', include(router.urls))
]
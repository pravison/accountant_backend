from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'inventories', views.InventoryView, 'inventory')
router.register(r'sold_products', views.SoldProductView, 'sold_products')

urlpatterns = [
    path('api/', include(router.urls)),
]
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'expenses', views.ExpenseView, 'expense')
router.register(r'payrols', views.PayrolView, 'payrol')
router.register(r'prepaidExpenses', views.PrepaidExpenseView, 'prepaidExpense')

urlpatterns = [
    path('api/', include(router.urls)),
]
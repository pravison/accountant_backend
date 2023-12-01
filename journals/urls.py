from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'transactions', views.TransactionView, 'transaction')
router.register(r'capitalWithdrawals', views.CapitalWithdrawalView, 'capitalwithdrawal')
router.register(r'loans', views.LoanView, 'loan')

urlpatterns = [
    path('api/', include(router.urls)),
]
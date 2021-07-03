from django.contrib import admin
from .models import (
    PaymentTransaction,
    PaymentMethod,
    TaskerWallet,
    TaskerPaymentAccount,
    CustomerWallet,
)

admin.site.register(TaskerPaymentAccount)
admin.site.register(CustomerWallet)
admin.site.register(TaskerWallet)
admin.site.register(PaymentTransaction)
admin.site.register(PaymentMethod)

# Register your models here.

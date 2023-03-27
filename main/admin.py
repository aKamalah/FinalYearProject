from django.contrib import admin
from .models import IncomeExpense

# Register your models here.

# CREATE ADMIN LOGIN: python manage.py createsuperuser. (Type In Terminal). And Fill Out Registration Form Provided In Terminal.
# REGISTER MODELS: Models Have To Be Registered So They Are Shown On The Admin Site. As Can Be Seen Below.
admin.site.register(IncomeExpense)

from django.contrib import admin
from . import models

@admin.register(models.Budget)
class BudgetAdmin(admin.ModelAdmin):
    search_fields = ['category__name']
    list_display = ['id', 'category', 'amount', 'start_date', 'end_date', 'status', 'user']
    list_filter = ['status', 'start_date']
    ordering = ['-start_date']
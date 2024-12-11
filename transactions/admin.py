from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    search_fields = ['note']
    list_display = ['id', 'category', 'amount', 'type', 'date', 'user']
    list_filter = ['type', 'date']
    ordering = ['-date']

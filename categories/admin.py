from django.contrib import admin
from . import models

@admin.register(models.Category)
class CategoriesAdmin(admin.ModelAdmin):
    search_fields = []
    list_display = ['id', 'name', 'type', 'user']
    list_display_links = ['id']
    list_filter = ['type', 'user']
    list_editable = []
    ordering = []

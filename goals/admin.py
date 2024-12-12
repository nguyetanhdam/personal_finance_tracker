from django.contrib import admin
from . import models

@admin.register(models.Goal)
class GoalAdmin(admin.ModelAdmin):
    search_fields = ["name"]
    list_display = ["id", "name", "target_amount", "saved_amount", "status", "deadline", "user"]
    list_filter = ["status", "deadline"]
    ordering = ["-deadline"]

from django.db import models
from categories.models import Category
from django.contrib.auth.models import User

class BudgetStatus(models.IntegerChoices):
    ACTIVE = 1, "Active"
    COMPLETED = 2, "Completed"
    EXCEEDED = 3, "Exceeded"

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True, db_index=True)
    amount = models.IntegerField(default=0, db_index=True)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=BudgetStatus.choices, default=BudgetStatus.ACTIVE)

    def __str__(self):
        return f"{self.category.name} ({self.get_status_display()['name']})"

    def get_status_display(self):
        for value, label in BudgetStatus.choices:
            if value == self.status:
                return {"id": value, "name": label}
        return {"id": None, "name": "Unknown Status"}

    def get_display_amount(self):
        return f"{self.amount:,}"

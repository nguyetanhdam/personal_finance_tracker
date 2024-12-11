from django.db import models
from django.contrib.auth.models import User

class TransactionType(models.IntegerChoices):
    INCOME = 1, "Income"
    EXPENSE = 2, "Expense"

class Category(models.Model):
    name = models.CharField(max_length=255)
    type = models.PositiveSmallIntegerField(choices=TransactionType.choices, default=TransactionType.INCOME)
    user = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)

    def __str__(self):
        return f"{self.name} ({self.get_type_display()})"
    
    def get_type_display(self):
        for value, label in TransactionType.choices:
            if value == self.type:
                return {"id": value, "name": label}
        return 'Unknown Type'
    
    class Meta:
        verbose_name = 'Categories'
        verbose_name_plural = 'Categories'

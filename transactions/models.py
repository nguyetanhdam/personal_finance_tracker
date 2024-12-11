from django.db import models
from categories.models import Category, TransactionType
from django.contrib.auth.models import User
from django.utils.timezone import now

class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, db_index=True)
    amount = models.IntegerField(default=0, db_index=True)
    type = models.IntegerField(choices=TransactionType.choices, default=TransactionType.INCOME)
    date = models.DateField(default=now, null=True, blank=True)
    note = models.TextField(null=True, blank=True, db_index=True)

    def __str__(self):
        return f"{self.get_type_display()['name']} - {self.amount}"

    def get_type_display(self):
        for value, label in TransactionType.choices:
            if value == self.type:
                return {"id": value, "name": label}
        return {"id": None, "name": "Unknown Type"}
from django.db import models
from django.contrib.auth.models import User

class GoalStatus(models.IntegerChoices):
    IN_PROGRESS = 1, "In Progress"
    ACHIEVED = 2, "Achieved"

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, db_index=True)
    name = models.CharField(max_length=255)
    target_amount = models.IntegerField(default=0, null=True, blank=True, db_index=True)
    saved_amount = models.IntegerField(default=0, null=True, blank=True, db_index=True)
    deadline = models.DateField(null=True, blank=True)
    status = models.IntegerField(choices=GoalStatus.choices, default=GoalStatus.IN_PROGRESS)

    def __str__(self):
        return f"{self.name} ({self.get_status_display()})"

    def get_status_display(self):
        for value, label in GoalStatus.choices:
            if value == self.status:
                return label
        return "Unknown Status"

    def update_status(self):
        """
        Update the goal status to 'Achieved' if saved_amount >= target_amount
        """
        if self.saved_amount >= self.target_amount and self.status != GoalStatus.ACHIEVED:
            self.status = GoalStatus.ACHIEVED
            self.save(update_fields=["status"])

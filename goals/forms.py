from django import forms
from .models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ["name", "target_amount", "saved_amount", "deadline", "status"]
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Goal Name"}),
            "target_amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Target Amount (VNĐ)"}),
            "saved_amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Saved Amount (VNĐ)"}),
            "deadline": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "status": forms.Select(attrs={"class": "form-select"}),
        }


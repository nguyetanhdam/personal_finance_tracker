from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ["category", "amount", "date", "note"]
        widgets = {
            "category": forms.Select(attrs={"class": "form-select"}),
            "amount": forms.NumberInput(attrs={"class": "form-control", "placeholder": "Amount (VNĐ)"}),
            "date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "note": forms.Textarea(attrs={"class": "form-control", "placeholder": "Note"}),
        }

    def clean_amount(self):
        amount = self.cleaned_data["amount"]
        try:
            return int(amount)
        except ValueError:
            raise forms.ValidationError("Invalid amount format. Please enter numbers only.")
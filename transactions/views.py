from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Transaction
from .forms import TransactionForm

@login_required
def transaction_list(request):
    transactions = Transaction.objects.filter(user=request.user).order_by("-date")
    return render(request, "transaction_list.html", {"transactions": transactions})

@login_required
def transaction_create(request):
    if request.method == "POST":
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.type = transaction.category.type
            transaction.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm()
    return render(request, "transaction_form.html", {"form": form})

@login_required
def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect("transaction_list")
    else:
        form = TransactionForm(instance=transaction)
    return render(request, "transaction_form.html", {"form": form})

@login_required
def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk, user=request.user)
    if request.method == "POST":
        transaction.delete()
        return redirect("transaction_list")
    return render(request, "transaction_confirm_delete.html", {"transaction": transaction})

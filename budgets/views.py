from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Budget
from .forms import BudgetForm

@login_required
def budget_list(request):
    budgets = Budget.objects.filter(user=request.user).order_by("-start_date")
    return render(request, "budget_list.html", {"budgets": budgets})

@login_required
def budget_create(request):
    if request.method == "POST":
        form = BudgetForm(request.POST)
        if form.is_valid():
            budget = form.save(commit=False)
            budget.user = request.user
            budget.save()
            return redirect("budget_list")
    else:
        form = BudgetForm()
    return render(request, "budget_form.html", {"form": form})

@login_required
def budget_update(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    if request.method == "POST":
        form = BudgetForm(request.POST, instance=budget)
        if form.is_valid():
            form.save()
            return redirect("budget_list")
    else:
        form = BudgetForm(instance=budget)
    return render(request, "budget_form.html", {"form": form})

@login_required
def budget_delete(request, pk):
    budget = get_object_or_404(Budget, pk=pk, user=request.user)
    if request.method == "POST":
        budget.delete()
        return redirect("budget_list")
    return render(request, "budget_confirm_delete.html", {"budget": budget})

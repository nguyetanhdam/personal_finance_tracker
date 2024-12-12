from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Goal
from .forms import GoalForm

@login_required
def goal_list(request):
    goals = Goal.objects.filter(user=request.user).order_by("-deadline")
    return render(request, "goal_list.html", {"goals": goals})

@login_required
def goal_create(request):
    if request.method == "POST":
        form = GoalForm(request.POST)
        if form.is_valid():
            goal = form.save(commit=False)
            goal.user = request.user
            goal.save()
            return redirect("goal_list")
    else:
        form = GoalForm()
    return render(request, "goal_form.html", {"form": form})

@login_required
def goal_update(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == "POST":
        form = GoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("goal_list")
    else:
        form = GoalForm(instance=goal)
    return render(request, "goal_form.html", {"form": form})

@login_required
def goal_delete(request, pk):
    goal = get_object_or_404(Goal, pk=pk, user=request.user)
    if request.method == "POST":
        goal.delete()
        return redirect("goal_list")
    return render(request, "goal_confirm_delete.html", {"goal": goal})

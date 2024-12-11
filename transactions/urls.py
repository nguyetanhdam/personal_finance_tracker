from django.urls import path
from . import views

urlpatterns = [
    path("", views.transaction_list, name="transaction_list"),
    path("create", views.transaction_create, name="transaction_create"),
    path("update/<int:pk>", views.transaction_update, name="transaction_update"),
    path("delete/<int:pk>", views.transaction_delete, name="transaction_delete"),
]
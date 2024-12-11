from django.contrib import admin
from django.urls import include, path
from categories import views as categories

urlpatterns = [
    path('admin/', admin.site.urls),
    path('categories/', include('categories.urls')),
    path('transactions/', include('transactions.urls')),
    path('', categories.category_list),
]

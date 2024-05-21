from django.urls import path
from . import views

urlpatterns = [
    path('productes/', views.producte_list, name='producte_list'),
    path('productes/<int:pk>/', views.producte_detail, name='producte_detail'),
    path('productes/create/', views.producte_create, name='producte_create'),
    path('productes/update/<int:pk>/', views.producte_update, name='producte_update'),
    path('productes/update/stock/<int:pk>/', views.producte_update_stock, name='producte_update_stock'),
    path('productes/delete/<int:pk>/', views.producte_delete, name='producte_delete'),
]

from django.urls import path
from . import views

urlpatterns = [
    path('productes/', views.producte_list, name='producte_list'),
    path('productes/<int:pk>/', views.producte_detail, name='producte_detail'),
    path('productes/create/', views.producte_create, name='producte_create'),
    path('productes/<int:pk>/update/', views.producte_update, name='producte_update'),
    path('productes/<int:pk>/delete/', views.producte_delete, name='producte_delete'),
]

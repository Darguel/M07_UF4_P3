from django.urls import path
from . import views

urlpatterns = [
    path('carreto/', views.carreto_list, name='carreto_list'),
    path('carreto/getProductes/<int:pk>', views.productesCarreto_list, name='getProductes_list'),
    # path('carreto/<int:pk>/', views.producte_detail, name='producte_detail'),
    path('carreto/create/', views.carreto_create, name='carreto_create'),
    path('carreto/addProducte/<int:pk>', views.carreto_addProducte, name='carreto_addProducte'),
    # path('carreto/update/<int:pk>/', views.producte_update, name='producte_update'),
    # path('carreto/update/stock/<int:pk>/', views.producte_update_stock, name='producte_update_stock'),
    # path('carreto/delete/<int:pk>/', views.producte_delete, name='producte_delete'),
]

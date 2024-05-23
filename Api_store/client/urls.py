from django.urls import path
from . import views

urlpatterns = [
    path('client/create/', views.client_create, name='client_create')
]

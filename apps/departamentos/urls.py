from django.urls import path
from .views import DepartamentosList, DepartamentoCreate, DepartamentoEdit, DepartamentoDelete

urlpatterns = [
    path('cadastro/list/', DepartamentosList.as_view(), name='list_departamento'),
    path('cadastro/new/', DepartamentoCreate.as_view(), name='create_departamento'),
    path('cadastro/update/<int:pk>/', DepartamentoEdit.as_view(), name='update_departamento'),
    path('cadastro/delete/<int:pk>/', DepartamentoDelete.as_view(), name='delete_departamento'),
]



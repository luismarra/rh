from django.urls import path
from .views import EmpresaCreate, EmpresaEdit

urlpatterns = [
    path('cadastro/new/', EmpresaCreate.as_view(), name='create_empresa'),
    path('cadastro/update/<int:pk>/', EmpresaEdit.as_view(), name='edit_empresa'),
]

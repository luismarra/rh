from django.urls import path
from .views import \
    FuncionariosList, \
    FuncionarioEdit, \
    FuncionarioNovo, \
    FuncionarioDelete


urlpatterns = [
    path('cadastro/list/', FuncionariosList.as_view(), name='list_funcionario'),
    path('cadastro/new/', FuncionarioNovo.as_view(), name='create_funcionario'),
    path('cadastro/delete/<int:pk>/', FuncionarioDelete.as_view(), name='delete_funcionario'),
    path('cadastro/update/<int:pk>/', FuncionarioEdit.as_view(), name='update_funcionario'),
]

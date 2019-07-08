from django.urls import path
from .views import DocumentoCreate, DocumentoEdit, DocumentoDelete

urlpatterns = [
    path('cadastro/new/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento_func'),
    path('cadastro/new/<int:pk>/', DocumentoCreate.as_view(), name='create_documento'),
    path('cadastro/edit/<int:pk>/', DocumentoEdit.as_view(), name='update_documento'),
    path('cadastro/delete/<int:pk>/', DocumentoDelete.as_view(), name='delete_documento'),
]



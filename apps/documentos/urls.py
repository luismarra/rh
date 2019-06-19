from django.urls import path
from .views import DocumentoCreate

urlpatterns = [
    path('cadastro/new/<int:funcionario_id>/', DocumentoCreate.as_view(), name='create_documento'),
]



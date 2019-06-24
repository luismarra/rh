from django.urls import path
from .views import \
    HoraExtraList, \
    HoraExtraEdit, \
    HoraExtraNovo, \
    HoraExtraDelete


urlpatterns = [
    path('cadastro/list/', HoraExtraList.as_view(), name='list_hora_extra'),
    path('cadastro/new/', HoraExtraNovo.as_view(), name='create_hora_extra'),
    path('cadastro/delete/<int:pk>/', HoraExtraDelete.as_view(), name='delete_hora_extra'),
    path('cadastro/update/<int:pk>/', HoraExtraEdit.as_view(), name='update_hora_extra'),
]

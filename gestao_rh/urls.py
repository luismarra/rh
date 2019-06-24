from django.conf import settings
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve


urlpatterns = [
    path('', include('apps.core.urls')),
    path('registro_horas_extras/', include('apps.registro_horas_extras.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]

if settings.DEBUG:
    urlpatterns += [
      url(r'^media/(?P<path>.*)$',
          serve, {'document_root':
                  settings.MEDIA_ROOT, }), ]

from django.contrib import admin
from .models import RegistroHoraExtra


"""
class RegistroHoraExtraAdmin(admin.ModelAdmin):
    fields = ['id', 'motivo', 'observacao', 'funcionario', 'date_time_he',
              'time_he1']
    search_fields = ['funcionario', 'motivo']
    list_filter = ['funcionario']
    list_display = ['id', 'motivo', 'funcionario', 'date_time_he',
              'time_he1']
    list_display_links = ['id', 'motivo']

admin.site.register(RegistroHoraExtra, RegistroHoraExtraAdmin)
"""
admin.site.register(RegistroHoraExtra)

from notas.models import Nota
from django.contrib import admin


class NotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'contenido', 'fecha_creacion', 'ultima_modificacion')

admin.site.register(Nota, NotaAdmin)
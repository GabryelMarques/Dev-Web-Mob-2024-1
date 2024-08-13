from django.contrib import admin
from gaps.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display= ['id', 'titulo', 'data', 'hora', 'local', 'descricao', 'foto','criador']
    search_fields = ['titulo']

admin.site.register(Evento, EventoAdmin)

from gaps.models import Inscricao

admin.site.register(Inscricao)

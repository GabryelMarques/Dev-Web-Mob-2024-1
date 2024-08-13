# gaps/urls.py

from django.urls import path
from django.contrib.auth import views as auth_views
from gaps.views import ListarEventos, FotoEvento, CadastrarEventos, ExcluirEvento, EditarEvento, cadastrar_cliente, user_profile, InscreverEvento, CancelarInscricaoView

urlpatterns = [
    path('', ListarEventos.as_view(), name='listar-eventos'),
    path('fotos/<str:arquivo>/', FotoEvento.as_view(), name='foto-evento'),
    path('add_evento/', CadastrarEventos.as_view(), name='cadastrar-eventos'),
    path('editar_evento/<int:pk>/', EditarEvento.as_view(), name='editar-evento'),
    path('excluir_evento/<int:evento_id>/', ExcluirEvento.as_view(), name='excluir-evento'),
    path('add_cliente/', cadastrar_cliente, name='cadastrar-cliente'),
    path('inscrever_evento/<int:evento_id>/', InscreverEvento.as_view(), name='inscrever-evento'),
    path('user_profile/', user_profile, name='user_profile'),
    path('cancelar_inscricao/<int:inscricao_id>/', CancelarInscricaoView.as_view(), name='cancelar-inscricao'),
]
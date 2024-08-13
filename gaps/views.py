from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404
from gaps.models import Evento, Inscricao
from django.core.exceptions import ObjectDoesNotExist
from django.http import FileResponse , Http404 
from gaps.forms import EventoForm, InscricaoForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from gaps.forms import PesquisaEventoForm
import logging

class ListarEventos(View):
    def get(self, request):
        form = PesquisaEventoForm(request.GET or None)
        termo_de_pesquisa = request.GET.get('termo_de_pesquisa', '')

        if termo_de_pesquisa:
            eventos = Evento.objects.filter(titulo__icontains=termo_de_pesquisa)
        else:
            eventos = Evento.objects.all().order_by('data')

        return render(request, 'gaps/listar_eventos.html', {'eventos': eventos, 'form': form})

    
class FotoEvento(View):
    def get(self, request, arquivo):
        try:
            evento = Evento.objects.get(foto='gaps/fotos/{}'.format(arquivo))
            return FileResponse(evento.foto)
        except ObjectDoesNotExist:
            raise Http404("Foto não encontrada ou nao autorizado!")
        except Exception as exception:
            raise exception
        
class CadastrarEventos(LoginRequiredMixin, View):
    def get(self, request):
        form = EventoForm()
        return render(request, 'gaps/add_evento.html', {'form': form})
    
    def post(self, request):
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.criador = request.user  # Definir o criador como o usuário logado
            evento.foto = request.FILES.get('foto', None)
            evento.save()
            return redirect('listar-eventos')
        return render(request, 'gaps/add_evento.html', {'form': form})

class ExcluirEvento(LoginRequiredMixin, View):
    def get(self, request, evento_id):
        evento = get_object_or_404(Evento, pk=evento_id)
        if evento.criador != request.user:
            return HttpResponseForbidden("Você não tem permissão para excluir este evento.")
        evento.delete()
        messages.success(request, 'Evento excluído com sucesso!')
        return redirect('listar-eventos')

from django.http import HttpResponseForbidden

class EditarEvento(LoginRequiredMixin, UpdateView):
    model = Evento
    form_class = EventoForm
    template_name = 'gaps/editar_evento.html'
    success_url = reverse_lazy('listar-eventos')

    def dispatch(self, request, *args, **kwargs):
        evento = self.get_object()
        if evento.criador != request.user:
            return HttpResponseForbidden("Você não tem permissão para editar este evento.")
        return super().dispatch(request, *args, **kwargs)


from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .forms import ClienteForm

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar-eventos')  
    else:
        form = ClienteForm()
    return render(request, 'gaps/add_cliente.html', {'form': form})

from django.contrib.auth.decorators import login_required
from .models import Inscricao
@login_required
def user_profile(request):
    user = request.user
    inscricoes = Inscricao.objects.filter(usuario=user)
    return render(request, 'gaps/user_profile.html', {'user': user, 'inscricoes': inscricoes})


logger = logging.getLogger(__name__)

class InscreverEvento(LoginRequiredMixin, View):
    def get(self, request, evento_id):
        evento = get_object_or_404(Evento, pk=evento_id)
        form = InscricaoForm(initial={'evento': evento})
        return render(request, 'gaps/inscrever_evento.html', {'form': form, 'evento': evento})

    def post(self, request, evento_id):
        evento = get_object_or_404(Evento, pk=evento_id)
        form = InscricaoForm(request.POST)
        if form.is_valid():
            logger.info('Formulário é válido')
            inscricao, created = Inscricao.objects.get_or_create(usuario=request.user, evento=evento)
            if created:
                messages.success(request, 'Inscrição realizada com sucesso!')
                logger.info(f'Inscrição criada para o usuário {request.user.username} no evento {evento.titulo}')
            else:
                messages.info(request, 'Você já está inscrito neste evento.')
                logger.info(f'Usuário {request.user.username} já está inscrito no evento {evento.titulo}')
            return redirect('listar-eventos')
        else:
            logger.error('Formulário inválido: %s', form.errors)
            messages.error(request, 'Erro na validação do formulário.')
        return render(request, 'gaps/inscrever_evento.html', {'form': form, 'evento': evento})


class CancelarInscricaoView(LoginRequiredMixin, View):
    def post(self, request, inscricao_id):
        inscricao = Inscricao.objects.filter(id=inscricao_id, usuario=request.user).first()
        if inscricao:
            inscricao.delete()
            messages.success(request, 'Inscrição cancelada com sucesso.')
        else:
            messages.error(request, 'Inscrição não encontrada ou você não tem permissão para cancelá-la.')
        return redirect('user_profile')
    

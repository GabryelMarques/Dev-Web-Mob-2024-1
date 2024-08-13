from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login, logout
from django.conf import settings
from django.contrib.auth import get_user_model

class Login(View):
    def get(self, request):
        contexto = {'mensagem': ''}
        if request.user.is_authenticated:
            return redirect("/gaps")
        else:
            return render(request, 'autenticacao.html', contexto)

    def post(self, request):
        # obtem as credenciais de autenticação do formulário
        email = request.POST.get('email', None)
        senha = request.POST.get('senha', None)
        
        # verificando as credenciais de autenticação fornecidas
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=email)
        except UserModel.DoesNotExist:
            user = None
        
        # Se o usuário existe, autentique com o nome de usuário e senha
        if user is not None:
            user = authenticate(request, username=user.username, password=senha)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("/gaps")
            return render(request, 'autenticacao.html', {'mensagem': 'Usuário inativo'})
        
        return render(request, 'autenticacao.html', {'mensagem': 'Email ou senha incorreta'})



class Logout(View):

    def get(self,request):
        logout(request)
        return redirect(settings.LOGIN_URL)
    
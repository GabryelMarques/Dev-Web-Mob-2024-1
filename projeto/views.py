from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,  login, logout
from django.conf import settings


class Login(View):

    def get(self,request):
        contexto = {'menssagem': ''}
        if  request.user.is_authenticated:
            return HttpResponse('Usuario ja esta logado!')
        else: 
            return render(request, 'autenticacao.html',contexto)
            #return redirect("/veiculos")
    

    def post(self, request):
    
        #obtem as credencias de autennticação do formulario
        usuario = request.POST.get('usuario', None )
        senha = request.POST.get('senha', None )
        # verificaca as credencias de autenticacao fornecidas 
        user = authenticate(request, username=usuario, password=senha)
        if user is not None: 
        #verifica se o usuario ainda esta ativo no sistema
            if user.is_active:
                login(request, user)
                return HttpResponse('Usuario autenticado com sucesso!')
               # return redirect("/veiculo")
            return render(request, 'autenticacao.html',{'mensagem': 'Usuario inatiovo '} )
        
        return render(request, 'autenticacao.html', {'mensagem': 'Usuario ou senha incorreta'})


class Logout(View):

    def get(self,request):
        logout(request)
        return redirect(settings.LOGIN_URL)
    
# gaps/models.py

from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(max_length=100, null=False, blank=False)
    descricao = models.TextField(null=False)
    data = models.DateField()
    hora = models.TimeField()
    local = models.CharField(max_length=200)
    foto = models.ImageField(blank= True, null=True, upload_to='gaps/fotos')
    criador = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{0} - {1} ({2}/{3})'.format(
            self.titulo,
            self.data,
            self.hora,
            self.local,
            self.descricao
        )

class Inscricao(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='inscricoes')
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='inscricoes')
    data_inscricao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} inscrito em {self.evento.titulo}"

from django.db import models
from django.utils import timezone
from six import string_types 
import datetime

class Questao(models.Model):
 questao_texto = models.CharField(max_length=200)
 pub_data = models.DateTimeField('data de publicacao')

 def __str__(self):
  return self.questao_texto
 
 def foi_publicada_recentemente(self):
  return self.pub_data >= timezone.now() - datetime.timedelta(days=1)

class Opcao(models.Model):
 questao = models.ForeignKey(Questao, on_delete=models.CASCADE)
 opcao_texto = models.CharField(max_length=200)
 votos = models.IntegerField(default=0)

 def __str__(self):
  return self.opcao_texto

from django.contrib.auth.models import User

class Aluno(models.Model):
 user = models.OneToOneField(User, on_delete=models.CASCADE)
 curso = models.CharField(max_length=100)
 votosFeitos = models.IntegerField(default=0)
 grupo = models.CharField(max_length=20, default=0)
 fotoPerfil = models.TextField(default="userdefault.png")
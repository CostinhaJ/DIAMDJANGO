import os
import django
from django.db.models import Q
from django.utils import timezone
import datetime

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DIAMDJANGO.settings')
django.setup()

# Now you can import Django models and run queries
from votacao.models import Questao, Opcao

# query a
questoes = Questao.objects.all()
list = []
for questao in questoes:
    list.append(questao.questao_texto)

print("\nQuery a:", list, "\n")


# query b
opcoes = Opcao.objects.filter(questao_id=3)
list = []
for opcao in opcoes:
    list.append(opcao.opcao_texto)

print("Query b:", list, "\n")

# query c
opcoes = Opcao.objects.filter(questao_id=3)
list = []
for opcao in opcoes:
    if(opcao.votos > 2):
        list.append(opcao.opcao_texto)

print("Query c:", list, "\n")

# query d
questao = Questao.objects.all()
list = []
for questao in questoes:
    if( questao.pub_data >= timezone.now() - datetime.timedelta(days=1096) ):
        list.append(questao)

print("Query d:", list, "\n")

# query e
opcoes = Opcao.objects.all()
cnt = 0
for opcao in opcoes:
    cnt += opcao.votos

print("Query e:", cnt, "\n")

# query f
questoes = Questao.objects.all()
list = []
curqstid=0

for questao in questoes:
    txt = questao.questao_texto
    max = 0
    nrvotos = 0
    opcaovotada = None
    opcoes = Opcao.objects.filter(questao_id=questao.id)

    for opcao in opcoes:
        nrvotos = opcao.votos
        if(max < nrvotos): max = nrvotos; opcaovotada = opcao

    list.append((questao.questao_texto, opcaovotada.opcao_texto))

print("Query f:", list, "\n")

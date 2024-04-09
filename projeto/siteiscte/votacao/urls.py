from django.urls import include, path
from . import views # (. significa que importa views da mesma directoria)

app_name = 'votacao'
urlpatterns = [
    # ex: votacao/
    path("", views.welcome, name='welcome'),

    path("", views.index, name='index'),
    # ex: votacao/1
    path('<int:questao_id>', views.detalhe, name='detalhe'),
    # ex: votacao/3/resultados
    path('<int:questao_id>/resultados', views.resultados, name='resultados'),
    # ex: votacao/5/voto
    path('<int:questao_id>/voto', views.voto, name='voto'),
    # ex: votacao/criarquestao
    path('criarquestao', views.criarquestao, name='criarquestao'),
    # ex: votacao/criarquestao2
    path('criarquestao2', views.criarquestao2, name='criarquestao2'),
    # ex: votacao/2/criaropcao
    path('<int:questao_id>/criaropcao', views.criaropcao, name='criaropcao'),
    # ex: votacao/2/criaropcao2
    path('<int:questao_id>/criaropcao2', views.criaropcao2, name='criaropcao2'),
    # ex: votacao/6/apagarquestao
    path('<int:questao_id>/apagarquestao', views.apagarquestao, name='apagarquestao'),
    # ex: votacao/6/apagaropcao
    path('<int:questao_id>/apagaropcao', views.apagaropcao, name='apagaropcao'),
    # ex: votacao/loginiscte
    path('loginiscte', views.loginiscte, name='loginiscte'),
    # ex: votacao/registar
    path('registar', views.registar, name='registar'),
    # ex: votacao/pessoal
    path('pessoal', views.pessoal, name='pessoal'),
    # ex: votacao/logoutiscte
    path('logoutiscte', views.logoutiscte, name='logoutiscte'),
]
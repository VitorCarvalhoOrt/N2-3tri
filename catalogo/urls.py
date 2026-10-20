from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    path('', views.pagina_inicial, name='home'),
    path('jogos/', views.pagina_inicial, name='lista_jogos'),
    path('jogos/novo/', views.novo_jogo, name='novo_jogo'),

    path('jogos/<int:pk>/', views.detalhes, name='detalhe_jogo'),
    path('jogos/<int:pk>/editar/', views.editar_jogo, name='editar_jogo'),
    path('jogos/<int:pk>/apagar/', views.eliminar_jogo, name='apagar_jogo'),
]
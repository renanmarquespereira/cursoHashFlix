# caminhos para crir uma pagina -- Url - view - template
from django.contrib.messages import success
from django.urls import path, reverse_lazy
from .views import Homepage, Homefilmes, Detalhefilme, Pesquisa_Filmes, EditarPerfil, CriarConta
from django.contrib.auth import views as auth_views

app_name = 'filme'

urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>/', Detalhefilme.as_view(), name='detalhefilme'),
    path('pesquisa/', Pesquisa_Filmes.as_view(), name='pesquisafilmes'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editar_perfil/<int:pk>/', EditarPerfil.as_view(template_name='editar_perfil.html'), name='editarperfil'),
    path('criar_conta/', CriarConta.as_view(template_name='criarconta.html'), name='criarconta'),
    #Success_lazy serve para redirecionar para uma outra pagina atraves daqui, sem precisar ir para classe nos views
    path('mudar_senha/', auth_views.PasswordChangeView.as_view(template_name='editar_perfil.html', success_url=reverse_lazy('filme:homefilmes')), name='mudarsenha'),
]
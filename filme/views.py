from django.db.models.fields import return_None
from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CriarContaForm, FormHome
# Function BASEVIEWS
#def homepage(request):
#    return render(request, 'homepage.html')

#def homefilmes(request):
#    context = {}
#    lista_filmes = Filme.objects.all()
#    context['lista_filmes'] = lista_filmes
#    return render(request, 'homefilmes.html', context)

#OU

# Class BASEVIEWS
class Homepage(FormView):
    template_name = 'homepage.html'
    form_class = FormHome

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuario = Usuario.objects.filter(email=email)


        if usuario:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme # cria uma lista chamada object_list

class Detalhefilme(LoginRequiredMixin, DetailView):
    template_name = 'detalhefilme.html'
    model = Filme # cria um item chamada object

    # contabilaza uma visualição atravaez da funcao get
    def get(self, request, *args, **kwargs):
        filme = self.get_object()
        filme.visualizacoes += 1
        filme.save()
        #Adiciona um filme visto para o usuario
        request.user.filmes_vistos.add(filme)
        #redireciona o usuario para url final
        return super().get(request, *args, **kwargs)
    #Pra vc colocar algum parametro no metodo context interno
    def get_context_data(self, **kwargs):
        context = super(Detalhefilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context

class Pesquisa_Filmes(LoginRequiredMixin, ListView):
    template_name = 'pesquisa_filmes.html'
    model = Filme

    # esta funcao serve para pegar alguma informação do html
    def get_queryset(self):
        # Neste caso pegamos o parametro Name do input html
        pesquisa = self.request.GET.get('query')
        if pesquisa:
            if pesquisa.lower() == 'todos':
                return self.model.objects.all()
            else:
                return self.model.objects.filter(titulo__icontains=pesquisa)
        else:
            return None


class CriarConta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')


class EditarPerfil(LoginRequiredMixin, UpdateView):
    template_name = 'editar_perfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')
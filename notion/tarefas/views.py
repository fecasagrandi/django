from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Usuario, Projeto, Tarefa  


def home_redirect(request):
    return redirect('usuarios_list')

class TarefaListView(ListView):
    model = Tarefa
    template_name = 'tarefas/tarefas_list.html'

class ProjetoListView(ListView):
    model = Projeto
    template_name = 'tarefas/projeto_list.html'

class UsuarioListView(ListView):
    model = Usuario
    template_name = 'tarefas/usuarios_list.html'  

class UsuarioCreateView(CreateView):
    model = Usuario
    fields = ['nome', 'email', 'funcao', 'status']
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuarios_list')

class UsuarioUpdateView(UpdateView):
    model = Usuario
    fields = ['nome', 'email', 'funcao', 'status']
    template_name = 'usuario_form.html'
    success_url = reverse_lazy('usuarios_list')

class UsuarioDeleteView(DeleteView):
    model = Usuario
    template_name = 'usuario_confirm_delete.html'
    success_url = reverse_lazy('usuarios_list')

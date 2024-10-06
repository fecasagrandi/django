from django.urls import path
from .views import UsuarioListView, UsuarioCreateView, UsuarioUpdateView, UsuarioDeleteView, ProjetoListView, TarefaListView

urlpatterns = [
    path('usuarios/', UsuarioListView.as_view(), name='usuarios_list'),
    path('usuarios/criar/', UsuarioCreateView.as_view(), name='usuario_create'),
    path('usuarios/<int:pk>/editar/', UsuarioUpdateView.as_view(), name='usuario_edit'),
    path('usuarios/<int:pk>/excluir/', UsuarioDeleteView.as_view(), name='usuario_delete'),
    path('projetos/', ProjetoListView.as_view(), name='projetos_list'),
    path('tarefas/', TarefaListView.as_view(), name='tarefas_list'),
]

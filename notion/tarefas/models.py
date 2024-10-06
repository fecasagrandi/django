from django.db import models

# Create your models here.

class Projeto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    data_inicio = models.DateField(default='2024-01-01')
    data_termino = models.DateField(default='2024-12-31')
    status = models.CharField(max_length=50, default='Pendente')

    def __str__(self):
        return self.nome

class Tarefa(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    data_criacao = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=[('Pendente', 'Pendente'), ('Em Progresso', 'Em Progresso'), ('Concluída', 'Concluída')])

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    tarefa = models.ForeignKey(Tarefa, on_delete=models.CASCADE)
    texto = models.TextField()
    autor = models.CharField(max_length=100)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.autor} - {self.tarefa.titulo}"

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    funcao = models.CharField(max_length=50)
    status = models.CharField(max_length=20, choices=[('Ativo', 'Ativo'), ('Inativo', 'Inativo')])

    def __str__(self):
        return self.nome
Gerenciador de Tarefas - Estilo Notion
Este é um projeto de Programação Avançada utilizando Django em Python. O objetivo é criar um gerenciador de tarefas no estilo Notion, com funcionalidades de CRUD (Create, Read, Update, Delete) para três tabelas. Este projeto faz parte de uma prática para o aprendizado avançado em desenvolvimento web com o framework Django.

Tecnologias Utilizadas
Python 3.12.7
Django 5.1
SQLite (banco de dados local padrão do Django)
HTML/CSS para o frontend básico
JavaScript para interações dinâmicas (futuramente)
Estrutura do Projeto
Este projeto está dividido nas seguintes seções:

Aplicativo Django: O projeto principal é um gerenciador de tarefas simples com três tabelas, que são:
Tarefas: Tabela principal onde você pode criar, editar, visualizar e excluir tarefas.
Categorias: Cada tarefa pertence a uma categoria (Ex.: Trabalho, Pessoal, Estudos).
Usuários: Gerenciamento dos usuários que podem ter suas próprias tarefas cadastradas.
Funcionalidades
O projeto inclui as seguintes funcionalidades:

CRUD Completo para as três tabelas:

Tarefas: Criar, listar, editar e excluir.
Categorias: Gerenciar as categorias associadas às tarefas.
Usuários: Gerenciar os usuários do sistema.
Administração: Django Admin configurado para facilitar a administração dos dados.

Interface Web: Interface básica para navegação e gerenciamento das tarefas com Django templates.

Validações de Formulários: Regras para validação de dados nas operações de criação e edição.

Configuração e Execução
Pré-requisitos
Certifique-se de ter os seguintes softwares instalados no seu sistema:

Python 3.12+
Pipenv ou pip (para gerenciar dependências)
Virtualenv (opcional, mas recomendado)
Passo a Passo
Clone o Repositório

Clone este repositório para sua máquina local:

bash
Copiar código
git clone https://github.com/SEU_USUARIO/gerenciador-tarefas-notion.git
Instale as Dependências

Navegue até o diretório do projeto e instale as dependências necessárias:

bash
Copiar código
pip install -r requirements.txt
Realize as Migrações

Após a instalação das dependências, realize as migrações do banco de dados:

bash
Copiar código
python manage.py migrate
Execute o Servidor de Desenvolvimento

Para rodar o projeto localmente, execute o comando:

bash
Copiar código
python manage.py runserver
O servidor estará disponível em: http://127.0.0.1:8000/

Acessar o Admin Django

Crie um superusuário para acessar o painel admin:

bash
Copiar código
python manage.py createsuperuser
Acesse o painel de administração em: http://127.0.0.1:8000/admin

Estrutura de Pastas
plaintext
Copiar código
meuAmbVir/
├── notion/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
├── tarefas/  # Aplicativo principal
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   ├── templates/
│   ├── static/
├── manage.py
Tabelas
Tarefas: Contém informações das tarefas criadas, como título, descrição, status, data de criação e prazo.
Categorias: Define categorias como Trabalho, Pessoal, Estudos, etc.
Usuários: Relaciona tarefas aos usuários que as criaram.
Próximos Passos
Melhorar a interface com Bootstrap ou Tailwind CSS.
Implementar um sistema de autenticação e login de usuários.
Adicionar funcionalidade de comentários ou subtarefas.
Incluir suporte a filtros e tags nas tarefas.
Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir Issues ou Pull Requests.

Licença
Este projeto está licenciado sob a MIT License.

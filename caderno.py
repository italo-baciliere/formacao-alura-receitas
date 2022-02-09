'''

______________________________________
DIVISÃO DAS AULAS
______________________________________
Iniciando aplicação e subindo o servidor
    Vamos preparar um ambiente virtual e subir o servidor

Template, rotas e views
    Vamos trabalhar com rotas e views no Django

Links, extends e partials
    Vamos refatorar nossas páginas html criando partials

Modelo e banco de dados
    Vamos configurar e conectar nossa aplicação Django com Postgres

Admin, parâmetros e receitas
    Utilizando o Django admin, vamos exibir as receitas do banco




______________________________________
DJANGO
______________________________________
Django utiliza o pdrão model-template-view (MTV)

Para trabalhar com o Django, primeiro, precisamos nos certificar que o
Python e o pip (gerenciador de pacotes do Python) estão instalados corretamente no seu computador.

Todas essas versões do Python incluem um banco de dados leve chamado SQLite,
para que você ainda não precise configurar um banco de dados.

No prompt de comando, digite 'python'
Dentro do terminal python, digite:
    >>> python --version
    >>> pip --version
    >>> python -m pip install --upgrade pip




INSTALANDO O DJANGO

No terminal do windows execute:
    $ pip install Django
No terminal interativo do Python, digite:
    >>> import django
    >>> print(django.get_version())

Comando django
    $ django-admin help




______________________________________
ESCREVEDO O SEU PRIMEIRO PROJETO
______________________________________

Um aplicativo do Django é um pacote separado em Python que contém
um conjunto de arquivos relacionados para uma finalidade específica.
Um projeto do Django pode conter qualquer número de aplicativos,
o que reflete o fato de que um host da Web pode servir qualquer número de pontos de
entrada separados de um único nome de domínio.
Nesse caso, o projeto do Django manipula o roteamento de URL e as configurações no
nível do site (nos arquivos urls.py e settings.py),
enquanto cada aplicativo tem seu próprio estilo e comportamento distintos por
meio de seus roteamentos, exibições, modelos, arquivos estáticos e interfaces administrativas internas.

    $ django-admin startproject <nome_do_projeto>
    $ django-admin.py startproject aprendendodjango

Criar projeto direto no diretório

    $ django-admin startproject <nome_do_projeto> .

Inicialiando o projeto

    $ python manage.py runserver

Estrutura do projeto:

    * __init__.py: arquivo vazio que indica um package. Diz ao Python que este diretório deve ser considerado um pacote.
    * settings.py: arquivo de configuração do projeto.
    * urls.py: todas as urls do projeto são definidas aqui.
    * wsgi.py: protocolo que serve http. Ponto de integração entre servidores

Crie o banco de dados antes de podermos usá-las. Para fazer isso, execute o seguinte comando:

    $ python manage.py migrate




______________________________________
APP
______________________________________

Um app é uma aplicação que realiza determinada função.
Por exemplo, uma visualização de receitas, devemos criar um app para essa visualização
Um app pode ser compartilhado entre diferentes projetos.

Ajudar do manage.py

    $ python manage.py help


INICIANDO UM APP
Inicie o app executando essa linha de comando:

    $ python manage.py startapp nome_do_app

Isso criará um diretório, que é apresentada desta forma:
    nome_do_app/
        __init__.py
        admin.py
        migrations/
            __init__.py
        models.py
        tests.py
        views.py


REGISTRANDO UM APP

Acesse a pastas 'apps.py' para verificar o nome do app recem criado

    name='receita'

Acesse o arquivo 'settings.py', insira o nome do app no atributo 'INSTALLED_APPS'


ACESSAR O APP

Crie um novo arquivo 'urls.py' na pasta do novo app
Import as 'urls' para o arquivo

    from django.urls import path

Importe todas as 'views' relacionadas a essa url
O arquivo de 'views' faz a manipulação de qual url será exibida na tela

    from . import views

Adicione no arquivo 'urls.py'

    urlpatterns = [
        path('', views.index, name='index')
    ]

Vamos criar a 'view'
Acesse o arquivo 'views.py' do seu app
Insire a função abaixo, mas antes, import o 'request':

    from django.http import HttpResponse

    def index(request):
        return HttpResponse('<h1>Receitas</h1>')

Antes de visualizarmos a view, devemos registrar as nossas rotas
Acesse o arquivo 'urls.py' do projeto
Inclua um 'path' dentro de 'urlpatterns', mas antes,
adicione o 'include' no import da '.urls'

    path('', include('receitas.urls')),





______________________________________
______________________________________
Criando um usuário administrador com o comando abaixo

    $ python manage.py createsuperuser

    - username: italo
    - Email address: italoluciano57@gmail.com
    - Password: pr0c0nc3pt

Agora, abra um navegador da Web e vá para "/ admin /" no seu domínio local -
por exemplo, http://127.0.0.1:8000/admin/




______________________________________
AMBIENTE VIRTUAL
______________________________________

python venv
https://docs.python.org/3/library/venv.html

Crie uma pasta para inserir o seu ambiente virtual

Criando um ambiente virtual
    $ python3 -m venv /path/to/new/virtual/environment

Estrutura do ambiente virtual
    /bin - arquivo necessário para carregar o ambiente virtual

Ativar o ambiente virtual
    Linux
    $ /path/to/new/virtual/environment/activate
    Windows
    $ /bin/activate/Scripts/activate.bat

Instalar o Django
    (environment) pip install django

Visualiar modulos instalados no ambiente virtual
    (environment) pip freeze

Atualizar o pip
    $ python -m pip install --upgrade pip




______________________________________
CONFIGURAÇÕES PROJETO
______________________________________

No arquivo 'settings.py' altere as seguintes propriedades

https://www.alura.com.br/artigos/timezone-no-django?gclid=Cj0KCQiAxoiQBhCRARIsAPsvo-xssBTyPKYoGLaOt0tIzU3ODGMRVziNKunM8KEgyv4_69VkDmm1iUIaAmi6EALw_wcB
https://github.com/guilhermeonrails/language_code_django/blob/list_languages/list.py
https://github.com/guilhermeonrails/language_code_django/blob/tz_list/list.py
https://docs.djangoproject.com/en/4.0/topics/i18n/
https://docs.djangoproject.com/en/3.0/topics/i18n/timezones/

    LANGUAGE_CODE
    TIME_ZONE




______________________________________
ESTUDAR - DETALHAR
______________________________________

Instrospecção
    - https://pt.wikipedia.org/wiki/Introspec%C3%A7%C3%A3o_%28computa%C3%A7%C3%A3o%29

Filosofia do Django segundo a documentação oficial
    - https://docs.djangoproject.com/pt-br/2.2/misc/design-philosophies/
'''




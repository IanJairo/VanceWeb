# VanceWeb

Para rodar:

Criar entorno virtual:
  $ python3 -m venv my_venv

Instalar pacotes:
  $ my_venv/bin/pip3 install -r requirements.txt
 
Entrar no Ambiente virtual:
  $ . my_venv/bin/activate
  
Atualizar banco:
  $ python3 manage.py db migrate
  $ python3 manage.py db upgrade

Iniciar plataforma:
  $ python3 run.py runserver

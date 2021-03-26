# VanceWeb

Para rodar:

Criar entorno virtual:
  $ python3 -m venv my_venv

Instalar pacotes(Linux):
  $ my_venv/bin/pip3 install -r requirements.txt

Instalar pacotes(Windows):
  $ python3 -m pip install -r requiremets.txt
 
Entrar no Ambiente virtual(Linux):
  $ . my_venv/bin/activate

Entrar no Ambiente virtual(Windows):
  $ .\my_venv\Scripts\activate
  
Atualizar banco:
  $ python3 run.py db migrate
  $ python3 run.py db upgrade

Iniciar plataforma:
  $ python3 run.py runserver

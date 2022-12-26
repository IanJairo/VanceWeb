# **VanceWeb**

## App Description

<p align="justify">Vance is a system of notes. With a login into the platform, all notes will be stored. In addition, it is possible to share specific notes with other users. </p>

## App Status:
![status](https://img.shields.io/badge/-FINALIZADO-brightgreen)

## Features:

| **INTERFACE:**                                            |
|-----------------------------------------------------------|
| - [ x ] CRUD                                              |
| - [ x ] Adding, editing and removing notes                |
| - [ x ] Share notes with other users                      |
| - [ x ] Share notes with other users                      |


## Technologies Employed:  

![Python](https://img.shields.io/badge/Python-blue)
![Flask](https://img.shields.io/badge/Flask-orange)<br>


## Requirements

1. Create virtual environment:  $ python3 -m venv my_venv

2. Instalar pacotes (Linux): $ my_venv/bin/pip3 install -r requirements.txt

2. Instalar pacotes (Windows):$ python3 -m pip install -r requirements.txt
 
3. Entrar no Ambiente virtual (Linux): $ . my_venv/bin/activate

3. Entrar no Ambiente virtual (Windows):  $ .\my_venv\Scripts\activate
  
4. Atualizar banco:
  $ python3 run.py db migrate && python3 run.py db upgrade

5. Iniciar plataforma:
  $ python3 run.py runserver

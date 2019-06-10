# WebAppStartWars
Applicación Web desarrollada en Python/Django para mostrar información varia del mundo de las galaxias.

# Instalación
git clone https://github.com/Darkvus/WebAppStarWars.git

or

Download Zip 

Una vez descargado el projecto en la raiz de la applicación deberemos de ejecutar el comando: pip3 install -r Requirements.txt

Una vex instalado los requesistos del proyecto debemos de ejecutar dos comandos para la creacion de nuestra base de datos con sqlite3.

En primer lugar ejecutamos python3 manage.py makemigrations y una vez este finalice ejecutamos python3 manage.py migrate.

Y tendremos todo lo necesario para lanzar nuestro servidor:
python3 manage.py runserver 

# Información
Con el boton carga de datos db localizado en el navbar de la aplicación nuestra base de datos se vera poblada con datos extrados de una api de Star Wars (https://swapi.co)


# Proyecto Final Menu Restaurante

Este Proyecto Final realizado por Dalma, Bryan y Walter, es una aplicacion Web para ser utilizada como Menu de Restaurante para hacer pedidos por parte del cliente y usuarios registrados
Se desarrrollo y programo en Python utilizando Django como Framework. 
Esta App web tiene diferentes  perfiles como admin, usuario con registro (Login)  y usuario sin Registro

Consta de Barras de Navegacion, Carrousel de imagenes, carrousel de opiniones y ofertas, Cards de Formas de pago, Cuadro colapsable de Como se usa y FAQ, un mapa de Google para Encuentranos, Formularios para Opiniones que se encuentra conectado con una cuenta de Gmail del Restaurante que envia un mail de confirmacion al cliente que su opinion fue registrada, un Pie de Pagina con informaciones y Links varios.

La barra de navegacion superior consta de diferentes botones para seleccionar las diferentes opciones del Menu en los cuales se puede hacer CRUD (Create, Read, Update y Delete)
Tambien gracias a Django se programo con HTML5 Y CSS3 que, combinado con las plantillas de Bootswatch y BooBootstrap nos facilitaron el diseño FrontEnd de este proyecto, para darle un aspecto mas user friendly.

Como Base de Datos se utilizo MySQL debido a que no tiene limites como SQLite y posee mayor nivel de seguridad

# Comenzando 🚀

Estas instrucciones te permitirán obtener una copia del proyecto en funcionamiento en tu máquina local para propósitos de desarrollo y pruebas.

(https://github.com/BryanRB519/Menu-Restaurante.git)

#  Descarga de instalación ZIP

Ir aL boton  “code” > download ZIP Descomprimir el archivo y luego elegir en que carpeta de tu equipo lo instalas y luego se abre con VS CODE

# Pre-requisitos 📋

Que cosas necesitas para instalar el software y como instalarlas

Deberas tener instalado para correr este proyecto:

Visual Studio Code, Python 3.12 o superior, Django 5.1.2, MySQL Workbench 8.0


# Instalación 🔧

Se instala en primer instancia VS Code, descargandola de https://code.visualstudio.com/download se elige el sistema operativo que usas Windows, Mac o Linux se descarga y se siguen los pasos que nos indica hasta terminar la instalacion.

Luego se instala Python , descargando de https://www.python.org/,  en la primer pantalla selecionar la caja de path sera de utilidad para este proyecto y luego seguir con la instalacion del mismo.

Se instala MySQL descargandolo de https://www.mysql.com/products/workbench/ siguendo los pasos hasta finalizar la instalacion

#  Comandos usados en la consola de VS CODE para hacer funcionar el proyecto

_python -m venv entorno (creamos el entorno virtual llamado "entorno")

.\entorno\Scripts\activate (activación del entorno virtual)

django-admin startproject MiProyecto (crea el proyecto)

cd .\MiProyecto\ (nos posiciona en la carpeta del proyecto)

python manage.py startapp MiApp (crea la app dentro de MiProyecto)

python manage.py makemigrations (hace los cambios en la base de datos y los modelos)

python manage.py migrate (Guarda los cambios de los modelos)

python manage.py runserver (activa el sitio web en localhost a la direccion http://127.0.0.1:8000/)

Con Ctrl+C se detiene la App

deactivate (desactiva el entorno)_

# Estructura de la App ⚙️

Desde VSC se abre una Carpeta que contiene los Archivos necesarios para correr la App

Aqui se describen los archivos mas importantes y como funcionan los mismos utilizando la arquitectura MVT (Models, Views, Templates)

Carpeta imagenes
    Donde se encuentran los archivos jpg que se visualizan en la Web

Archivo styles.css donde se programan los efectos visuales de color, estilo, movimiento etc que se ven en las diferentes partes de la Web

![image](https://github.com/user-attachments/assets/fd41c1f7-6120-4d73-8557-cb2af5ec5a7b)

Carpeta Templates/App
   Aqui se encuentran los archivos html donde se definen las Clases que representan los Objetos con sus Propiedades, Argumentos e Instancias que componen la App
   Los html mas importantes son el Base y el Index 

   El Base.html posee la Barra de Navegacion principal, el vinculo con el archivo style.css mencionado antes, la configuracion basica de diseño obtenido en bootswatch, la imagen del icono de la ventana (favicon), varias Clases donde se vincula los Botones de la barra principal (navbar) con las URLs de dichos Botones. Dichas Urls estan definidas en el campo "name=" en los path del archivo urls.py
   
   Se define aqui que Botones se visualizan estando o no logueados
   Tambien se configura la Herencia con otros archivos HTML para reducir la cantidad de codigo HTML necesario de escribir  en los mismos
   
   El Index.html hereda la cofiguracion incicial del archivo Base y posee la configuracion inicial de la pagina principal que aparece cada vez que se abre la App
   
   Se definen varias Clases cuyos atributos y metodos se utilizan para configurar diferentes partes y contenedores de la App Web como ser:
   
   El Banner /    Carrousel de las imagenes que estan en la carpeta Static/App/imagenes /   Carrousel de Testimonios y Promociones /     Cards de Formas de pago  /  Seccion de Como se usa y FAQ con textos colapsables  /     Link de Google Maps con ubicacion  /   Seccion de Formulario para Mensajes y Opinion viculado con path en url.py  /     Seccion de Pie de pagina (Footer) con datos varios y link con RRSS
       

![image](https://github.com/user-attachments/assets/71b42346-78fa-4ef0-ba9f-40659f9d2ea0)

En models.py se crean las Clases que representan las tablas que se cargan en la base de datos MySQL con todos los Objetos y sus atributos (Bebidas,Comidas, Postres, etc)
Se importan de Django.db los models para conectarlos con la BD

![image](https://github.com/user-attachments/assets/34c41a32-69dc-4de3-ae28-e6f96ab4a25d)


En admin.py se conectan los Models con el Administrador de Django

![image](https://github.com/user-attachments/assets/d5195e76-6e5a-477b-862b-772320d74ff3)


El view.html se importan varias funciones y modulos de Django pero principalmente se importan los Models y las funciones render y redirect para que rendericen los HTML y muestren la pagina

Tambien principalmente se definen las funciones "def" (mostrar,crear,buscar,actualizar y eliminar) necesarias para el CRUD de todas las "clases" generadas en el archivo models.py y se retornan renderizando a cada archivo html de cada uno de los Objetos

![image](https://github.com/user-attachments/assets/7f978d9a-f946-4d68-9d1d-f93b3ea583f3)



![image](https://github.com/user-attachments/assets/e60901d2-aaf6-495f-93aa-f771d139ae78)





## Versionado 📌

Version Inicial sin subir a host, solo en modo local

## Autores ✒️

Bryan, Dalma y Walter

## Licencia 📄

Esta App no esta licenciada

## Expresiones de Gratitud 🎁
Al profe Ignacio por su dedicacion y esfuerzo por explicar todos los temas



---


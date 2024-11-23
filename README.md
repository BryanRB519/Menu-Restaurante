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

PONER LINK DE GIT CLONE """"""""""""""""

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

   El Base posee la Barra de Navegacion principal, el vinculo con el archivo style.css mencionado antes, la configuracion basica de diseño obtenido en bootswatch, la imagen del icono de la ventana (favicon), varias Clases donde se vincula los Botones de la barra principal (navbar) con las URLs de dichos Botones. Dichas Urls estan definidas en el campo "name=" en los path del archivo urls.py
   Se define aqui que Botones se visualizan estando o no logueados
   Tambien se configura la Herencia con otros archivos HTML para reducir la cantidad de codigo HTML necesario de escribir  en los mismos
   El Index hereda la cofiguracion incicial del archivo Base y posee la configuracion inicial de la pagina principal que aparece cada vez que se abre la App
   Se definen varias Clases cuyos atributos y metodos se utilizan para configurar diferentes partes y contenedores de la App Web como ser:
   El Banner
   Carrousel de las imagenes que estan en la carpeta Static/App/imagenes
   Carrousel de Testimonios y Promociones
   Cards de Formas de pago
   Seccion de Como se usa y FAQ con textos colapsables
   Link de Google Maps con ubicacion
   Seccion de Formulario para Mensajes y Opinion viculado con path en url.py
   Seccion de Pie de pagina (Footer) con datos varios y link con RRSS
       

![image](https://github.com/user-attachments/assets/71b42346-78fa-4ef0-ba9f-40659f9d2ea0)



### Analice las pruebas end-to-end 🔩

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

### Y las pruebas de estilo de codificación ⌨️

_Explica que verifican estas pruebas y por qué_

```
Da un ejemplo
```

## Despliegue 📦

_Agrega notas adicionales sobre como hacer deploy_

## Construido con 🛠️

_Menciona las herramientas que utilizaste para crear tu proyecto_

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - El framework web usado
* [Maven](https://maven.apache.org/) - Manejador de dependencias
* [ROME](https://rometools.github.io/rome/) - Usado para generar RSS

## Contribuyendo 🖇️

Por favor lee el [CONTRIBUTING.md](https://gist.github.com/villanuevand/xxxxxx) para detalles de nuestro código de conducta, y el proceso para enviarnos pull requests.

## Wiki 📖

Puedes encontrar mucho más de cómo utilizar este proyecto en nuestra [Wiki](https://github.com/tu/proyecto/wiki)

## Versionado 📌

Usamos [SemVer](http://semver.org/) para el versionado. Para todas las versiones disponibles, mira los [tags en este repositorio](https://github.com/tu/proyecto/tags).

## Autores ✒️

_Menciona a todos aquellos que ayudaron a levantar el proyecto desde sus inicios_

* **Andrés Villanueva** - *Trabajo Inicial* - [villanuevand](https://github.com/villanuevand)
* **Fulanito Detal** - *Documentación* - [fulanitodetal](#fulanito-de-tal)

También puedes mirar la lista de todos los [contribuyentes](https://github.com/your/project/contributors) quíenes han participado en este proyecto. 

## Licencia 📄

Este proyecto está bajo la Licencia (Tu Licencia) - mira el archivo [LICENSE.md](LICENSE.md) para detalles

## Expresiones de Gratitud 🎁

* Comenta a otros sobre este proyecto 📢
* Invita una cerveza 🍺 o un café ☕ a alguien del equipo. 
* Da las gracias públicamente 🤓.
* Dona con cripto a esta dirección: `0xf253fc233333078436d111175e5a76a649890000`
* etc.



---
⌨️ con ❤️ por [Villanuevand](https://github.com/Villanuevand) 😊

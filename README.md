# Meraki, Ansible y Docker.

## Información del proyecto:

Este proyecto tiene como objetivo automatizar la ejecución de una consulta de acceso a la API de meraki para automatizar el proceso de inventario de dispositivos conectados a una organización y generar un archivo CSV cada 5 minutos, utilizando Docker para contenerizar la aplicación y garantizar su portabilidad y reproducibilidad.

Estaremos trabajando directamente con la API publica de Meraki, por lo que accederemos a una información que es publica. 

## Estructura del proyecto:

- Dockerfile: Define la imagen Docker, incluyendo la instalación de dependencias y el punto de entrada de la aplicación.
- docker-compose.yml: Define los servicios y volúmenes para ejecutar la aplicación utilizando Docker Compose.
- p2meraki_inventory.py: Contiene el código Python principal que ejecuta la consulta y genera el CSV.
- requirements.txt: Lista las dependencias de Python.

## Descripción del Script:

Este codigo esta conformado por tres funciones principales: getOrganizations(), getOrganizationsDevices(org_id) y GetInventory(). Además, requiere el URL del API publica de Meraki y la API_KEY de acceso.

- getOrganizations(): Esta funcion se encarga de acceder a la información de la organizacion a la cual se tiene acceso mediante la API_KEY. La información que es obtiene es: id, licesing, management, name y url.

- getOrganizationsDevices(org_id): Esta función se encarga de obtener la información de los dispositivos que están conectados a una organización. Esta función requiere el id de la organización para poder obtener la información de los equipos.

- GetInventory(): Se encarga de crear el archivo .csv con la información solicitada de los equipos. El archivo .csv es un inventario de todos los equipos de tipo "wireless" y "appliance" en todas las redes de la organización, y contiene: modelo del equipo, nombre, dirección MAC, dirección IP pública y de la LAN, número serial y status del dispositivo.

## Requisitos:

Debes asegurarte de tener instaladas las siguientes dependencias en tu ordenador:

- Python 3.
- Las librería requests.
- Ansible.
- Docker.
- Git.

## Instalación de Dependencias:

### Instalación de Python:

- Desde la página web de Python:

1. Descarga Python: Ve al sitio web oficial de Python (python.org) y descarga la versión más reciente de Python para tu ordenador, sea Windows o MAC.

2. Instalación: Ejecuta el instalador descargado y sigue las instrucciones en pantalla. Asegúrate de marcar la opción "Add Python to PATH" para que puedas ejecutar Python desde la terminal o simbolo del sistema.

### Instalación de la librería requests:

- Desde la terminal o simbolo del sistema:
  
1. Abre la terminal o simbolo del sistema.
   
2. Ejecuta el siguiente comando:
   
   pip install requests

3. Puedes verificar la instalación de la libreria con el siguiente comando:

   pip show requests

### Instalación de la librería requests mediante el archivo requirements.txt:

1. Abre la terminal o simbolo del sistema.
   
2. Accede a la carpeta donde está ubicado el archivo requirements.txt,

   por ejemplo:  cd C:\Users\user\Documents\p2_meraki
   
4. Ejecuta el siguiente comando:
   
   pip install -r requirements.txt

### Como usar el codigo:

En el proyecto p2 la ejecución del codigo dependía de ejecutar p2meraki.py para descargar el inventario requerido. Ahora, al integrarlo con Docker seremos capaces de crear un contender que se ejecute en segundo plano y haga las consultas del inventario cada cinco (5) minutos, esto nos ayudará a mantener nuestro inventario siempre actualizado.

1. Lo primero es abrir la terminal o simbolo del sistema.
   
2. Luego se debe clonar el repositorio de GitHub, puedes hacerlo mediante el comando:

   git clone https://github.com/SoyKenMendoza/Meraki_EC5756
    
3. Accede a la carpeta donde está ubicado el archivo, por ejemplo:  cd C:\Users\user\Documents\Meraki_EC5756
   
4. Luego ejectuar el comando: docker-compose up -d
   
5. El comando anterior se encargará de buscar y ejecutar el archivo "docker-compose.yml". El cual a su vez se encargará de ejecutar el archivo Dockerfile para crear el contenedor de nuestra practica.
   
6. Si deseas navegar dentro de los archivos del contenedor puedes usar el comando:

   docker exec -it docker_p3 bash

   Esto te permitirá ingresar al contenedor como si estuvieras en una terminal dentro de él. Una vez dentro, puedes usar    comandos como ls para listar los archivos en un directorio específico, cd para cambiar de directorio y cualquier otro    comando de tu sistema operativo.

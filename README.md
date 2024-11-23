# Meraki_EC5756

## Información del proyecto:

Este proyecto esta diseñado con Python y nos permite tener acceso a la API de meraki para automatizar el proceso de inventario de dispositivos conectados a una organización.

Estaremos trabajando directamente con la API publica de Meraki, por lo que accederemos a una información que es publica. 

## Requisitos:

Debes asegurarte de tener instaladas las siguientes dependencias en tu ordenador:

- Python 3.
- Las librería requests.

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

### Como usar el codigo:

1. Lo primero que debes saber es la ubicación y el nombre del archivo .py con el que estamos trabajando. En nuestro caso es p2meraki.py
   
2. Abrir la terminal o simbolo del sistema.
   
3. Accedere a la carpeta donde está ubicado el archivo, por ejemplo:  cd C:\Users\user\Documents\p2_meraki
   
4. En este punto, te recomiendo crear un entorno virtual de python para trabajar con mayor seguridad. Para ello debes ejecturar el siguiente comando:
   
   python -m venv nombre_entorno
   
5. Luego de creardo el entorno, debes activarlo con el comando a continuación:

   nombre_entorno\Scripts\activate

6. Ejecutar el archivo con:

    python p2meraki.py

NOTA: Si aparece el siguiente error al ejecutar el archivo: "ModuleNotFoundError: No module named 'requests'", te recomiendo instalar la libreria request luego del paso 5. Es posible que no encuentre instalada directamente en tu entorno virtual de Python creado.

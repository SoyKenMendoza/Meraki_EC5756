#Version de ubuntu base
FROM ubuntu:latest

#Carpeta donde se encuentran los archivos
WORKDIR /meraki_p3

#Crea el volumen necesario para almacenar el archivo CSV
VOLUME /meraki_p3_data

#Instala pip y venv para Python 3
RUN apt-get update && apt-get install -y python3-pip python3-venv

#Crea un entorno virtual llamado "venv"
RUN python3 -m venv venv

#Copia el archivo requirements.txt dentro del contenedor
COPY requirements.txt requirements.txt

#Activa el entorno virtual e instala las dependencias
RUN venv/bin/pip install -r requirements.txt

#Copia el resto de los archivos del proyecto
COPY . .

#Ejectua el script principal
CMD ["venv/bin/python", "p2meraki_inventory.py"]
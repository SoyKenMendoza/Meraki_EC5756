import requests
import csv
import time
from pprint import pprint

#Global Parameters

url = 'https://api.meraki.com/api/v1'

payload = None

API_KEY = '75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6'

headers = {

        "Authorization": "Bearer 75dd5334bef4d2bc96f26138c163c0a3fa0b5ca6",
        "Accept": 'application/json'
    }

#Get Organization

def getOrganizations():

    response = requests.request('GET',f"{url}/organizations", headers=headers, data = payload)
    response.raise_for_status()
    return response.json()

#Get Devices

def getOrganizationsDevices(org_id):

   response = requests.request('GET', f"{url}/organizations/{org_id}/devices", headers=headers, data = payload)
   response.raise_for_status()
   return response.json()

#Get Inventory

def GetInventory ():

    #Definimos un listado con el nombre de las columnas del archivo
    fieldnames = ['Model', 'Name', 'MAC Address', 'Public IP', 'LAN IP', 'Serial', 'Status']

    #Creamos el archivo
    with open('InventoryMeraki.csv', mode='w', newline='') as file:

        writer = csv.DictWriter(file, delimiter=',', fieldnames=fieldnames)

        #Generamos la primera fila con el nombre de las columnas.
        writer.writeheader()

        #Convertimos la respuesta de Json en un diccionario para Organization
        organizations = getOrganizations()

        #Hacemos busqueda de la Organizacion
        for org in organizations:

            #Convertimos la respuesta de Json en un diccionario para Devices
            devices = getOrganizationsDevices(org['id'])

            #Comenzamos la escritura de los disposiivos
            for dev in devices:

                #Buscamos los dispositivos de tipo "wireless" (MR) y "appliance" (MX)
                if 'MR' in dev['model'] or 'MX' in dev['model']:
                    writer.writerow({
                    'Model': dev.get('model', 'N/A'),
                    'Name': dev.get('name', 'N/A'),
                    'MAC Address': dev.get('mac', 'N/A'),
                    'Public IP': dev.get('publicIp', 'N/A'),
                    'LAN IP': dev.get('lanIp', 'N/A'),
                    'Serial': dev.get('serial', 'N/A'),
                    'Status': dev.get('status', 'N/A')
                    })

##Main

while True:
    GetInventory ()
    time.sleep(300) 

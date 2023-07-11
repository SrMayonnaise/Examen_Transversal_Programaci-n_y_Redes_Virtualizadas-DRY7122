import urllib.parse
import requests
from datetime import datetime

main_api = "https://www.mapquestapi.com/directions/v2/optimizedroute?"
key = "8Ra7mwRfWWH2a93KngLFPaTJybmrqIBS"

while True:
 
    hora = datetime.now()
    HF = hora.strftime("%H:%M")
    print ("Bienvenido a Mapquest",HF)

    orig = input ('Ciudad de Origen: ')
    if orig == 'Salir' or orig == 'S':
        break
    dest = input ('Ciudad de Destino: ')
    if dest == 'Salir' or dest == 'S':
        break
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest, "locale": "es_ES"})
    print('URL: ' + url)

    json_data = requests.get(url).json()
    json_status = json_data["info"] ["statuscode"]
    #print(json_data)

    if json_status == 0:
        print("API STATUS: " + str(json_status) + " = Llamada a la API exitosa.\n")
        print("=============================================")
        print("Direcciónes de " + orig + " hasta " + dest)
        print("Duración del viaje: " + json_data["route"]["formattedTime"])
        print("Kilómetros: {:.1f}".format(json_data["route"]["distance"] * 1.61))

        if "fuelUsed" in json_data["route"]:
            print("Fuel Used (Ltr): {:.1f}".format(json_data["route"]["fuelUsed"] * 3.78))
        else:
            print("La información del combustible no se encuentra disponible se encuentra deprecada.")

        print("=============================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            distance_km = each["distance"] * 1.61
            print(each["narrative"] + " ({:.1f} km)".format(distance_km))
        print("=============================================\n")

    elif json_status == 402:
        print("**********************************************")
        print("Status Code: " + str(json_status) + "; Ubicación no válida para la primera o segunda, vuelva a ingresar.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("For Status Code: " + str(json_status) + "; Refer to:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")

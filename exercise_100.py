# Vamos a hacer un ejercicios para base de datos

import requests

#### Conexion a base de datos ###
api_request = requests.get("https://open.er-api.com/v6/latest/PEN")
api_data = api_request.json()

### Titulo ###
print("--- De Soles a dolares ---")

#### Peticion ####
while True:
    try:
        user_request = float(input("Eliga la cantidad de soles: ")) ; break
    except:
        print("Solo se aceptan numeros")

### Transformacion ####
transformation = float(api_data["rates"]["USD"]) * user_request
print(f"Su valor es: {transformation}")

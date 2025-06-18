import requests
import json

# Endpoint para Patient
url = "https://hapi.fhir.org/baseR4/Patient"

# Datos del paciente
data = {
    "resourceType": "Patient",
    "identifier": [
        {
            "system": "http://dni.argentina.gov",
            "value": "43243418"
        }
    ],
    "name": [
        {
            "use": "official",
            "family": "Resnik",
            "given": ["Josefina"]
        }
    ],
    "gender": "female",
    "birthDate": "2001-04-28"
}

headers = {
    "Content-Type": "application/fhir+json"
}

# POST para crear el paciente
response = requests.post(url, headers=headers, json=data)

print("Código de respuesta:", response.status_code)
response_json = response.json()
print(json.dumps(response_json, indent=2))

# Leer el paciente creado
patient_id = response_json.get("id")
if patient_id:
    print(f"\nRecurso disponible en:")
    print(f"https://hapi.fhir.org/baseR4/Patient/{patient_id}/_history/1")

    get_url = f"https://hapi.fhir.org/baseR4/Patient/{patient_id}"
    get_response = requests.get(get_url)
    print("\nLectura del recurso creado:")
    print(json.dumps(get_response.json(), indent=2))
else:
    print("No se pudo obtener el ID del paciente.")

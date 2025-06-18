import requests
import json

# URL del endpoint Procedure
url = "https://hapi.fhir.org/baseR4/Procedure"

# ID del paciente creado en actividad 3a
patient_id = "47930665"

# Datos del recurso Procedure
procedure = {
    "resourceType": "Procedure",
    "status": "completed",
    "code": {
        "text": "Extracción de muela del juicio"
    },
    "subject": {
        "reference": f"Patient/{patient_id}"
    },
    "performedDateTime": "2024-06-01",
    "note": [
        {
            "text": "La extracción fue realizada sin complicaciones."
        }
    ]
}

headers = {
    "Content-Type": "application/fhir+json"
}

# POST para crear el recurso
response = requests.post(url, headers=headers, json=procedure)

print("Código de respuesta:", response.status_code)
response_json = response.json()
print(json.dumps(response_json, indent=2))

# Mostrar la URL del recurso creado
procedure_id = response_json.get("id")
if procedure_id:
    print(f"\nRecurso Procedure creado en:")
    print(f"https://hapi.fhir.org/baseR4/Procedure/{procedure_id}/_history/1")
else:
    print("No se pudo obtener el ID del procedimiento.")
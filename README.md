# TP6 - Interoperabilidad

## Materia
**Informática Médica 16.22 – 1C2025**  

- **Josefina Resnik** – Legajo: 61214
- **Ailín L. R. Arakaki** – Legajo: 56387

## Objetivo

Este repositorio contiene las soluciones correspondientes a la **Actividad 3 del TP6**, que consistió en el uso de recursos FHIR mediante código Python y la interacción con el servidor público de **HAPI FHIR**.

## Actividades

### Actividad 3a – Crear y leer un recurso `Patient`

Archivo: [`paciente10.py`](paciente10.py)  
Se creó un paciente con documento, nombre, género y fecha de nacimiento.  
Se leyó el recurso inmediatamente después de su creación.

### Actividad 3b – Buscar paciente por documento

Archivo: [`buscarpaciente10.py`](buscarpaciente10.py)  
Se implementó una búsqueda por `identifier` para recuperar al paciente creado en 3a.

### Actividad 3c – Crear un recurso `Procedure` relacionado

Archivo: [`procedure10.py`](procedure10.py)  
Se creó un recurso del tipo `Procedure`, vinculado al paciente anterior mediante el campo `subject`.

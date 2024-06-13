import csv
import json

def cargar_proyectos():
    proyectos = []
    try:
        with open("Proyectos.csv", newline='', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            for fila in lector_csv:
                proyecto = {
                    'id': int(fila['id']),  # Convertir el ID a entero si es necesario
                    'Nombre del Proyecto': fila['Nombre del Proyecto'],
                    'Descripción': fila['Descripción'],
                    'Fecha de inicio': fila['Fecha de inicio'],
                    'Fecha de Fin': fila['Fecha de Fin'],
                    'Presupuesto': float(fila['Presupuesto']),  # Convertir el presupuesto a float si es necesario
                    'Estado': fila['Estado']
                }
                proyectos.append(proyecto)
    except FileNotFoundError:
        print("El archivo 'Proyectos.csv' no fue encontrado.")
    except csv.Error as e:
        print(f"Error CSV al cargar proyectos desde 'Proyectos.csv': {e}")
    except Exception as e:
        print(f"Ocurrió un error al cargar los proyectos desde 'Proyectos.csv': {e}")
    
    return proyectos


def guardar_proyectos_csv(proyectos: list):
    fieldnames = ["id", "Nombre del Proyecto", "Descripción", "Fecha de inicio", "Fecha de Fin", "Presupuesto", "Estado"]
    
    with open('Proyecto_csv.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        
        for proyecto in proyectos:
            writer.writerow({
                "id": proyecto["id"],
                "Nombre del Proyecto": proyecto["Nombre del Proyecto"],
                "Descripción": proyecto["Descripción"],
                "Fecha de inicio": proyecto["Fecha de inicio"],
                "Fecha de Fin": proyecto["Fecha de Fin"],
                "Presupuesto": proyecto["Presupuesto"],
                "Estado": proyecto["Estado"]
            })
    
def guardar_proyectos_json(proyectos: list):
    # Nombre del archivo donde se guardará la información
    json_filename = 'Proyecto_json.json'

    # Escribir la lista de proyectos en el archivo JSON
    with open(json_filename, 'w') as json_file:
        json.dump(proyectos, json_file, indent=4)
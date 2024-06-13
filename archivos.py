import csv
import json

def cargar_proyectos():
    """
    La función `cargar_proyectos` lee los datos del proyecto desde un archivo CSV y devuelve una lista
    de diccionarios que representan los proyectos.
    :return: The function `cargar_proyectos()` is returning a list of dictionaries where each dictionary
    represents a project with the following keys: 'id', 'Nombre del Proyecto', 'Descripción', 'Fecha de
    inicio', 'Fecha de Fin', 'Presupuesto', and 'Estado'.
    """
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
    """
    La función `guardar_proyectos_csv` toma una lista de proyectos y escribe sus detalles en un archivo
    CSV con nombres de campos específicos.
    
    :param proyectos: Parece que estás intentando escribir una lista de proyectos en un archivo CSV
    usando la función proporcionada `guardar_proyectos_csv`. La función toma una lista de proyectos como
    entrada y los escribe en un archivo CSV llamado "Proyecto_csv.csv" con nombres de campos específicos
    :type proyectos: list
    """
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
    """
    La función `guardar_proyectos_json` guarda una lista de proyectos en un archivo JSON con una sangría
    de 4 espacios.
    
    :param proyectos: Se espera que el parámetro `proyectos` en la función `guardar_proyectos_json` sea
    una lista de proyectos que desea guardar en un archivo JSON. Cada proyecto de la lista debe estar en
    un formato que pueda serializarse en JSON, como un diccionario. La función escribirá
    :type proyectos: list
    """
    json_filename = 'Proyecto_json.json'

    with open(json_filename, 'w') as json_file:
        json.dump(proyectos, json_file, indent=4)
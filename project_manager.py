import utils as ut
import datetime
import copy
def Agregar_proyecto(proyectos: list):
    if len(proyectos) >= 50:
        print("No se pueden agregar más proyectos. Límite alcanzado.")
        return

    proyecto_id = len(proyectos) + 1
    nombre = ut.get_validar_string("Nombre del Proyecto (solo caracteres alfabéticos, máx 30): ", 30, alpha_only=True)
    decripcion = ut.get_validar_string("Descripción (alfanumérico, máx 200): ", 200)
    presupuesto = ut.get_validar_int("Presupuesto (mínimo $500000): ", 500000)
    fechaInicio = ut.get_validar_date("Fecha de Inicio (DD/MM/AAAA): ")
    fechaFin = ut.get_validar_date("Fecha de Fin (DD/MM/AAAA): ", fechaInicio)
    
    proyecto = {
        "id": proyecto_id,
        "Nombre del Proyecto": nombre,
        "Descripción": decripcion,
        "Presupuesto": presupuesto,
        "Fecha de inicio": fechaInicio.strftime("%d/%m/%Y"),
        "Fecha de Fin": fechaFin.strftime("%d/%m/%Y"),
        "Estado": "Activo"
    }
    
    proyectos.append(proyecto)
    print(f"Proyecto '{nombre}' agregado exitosamente.")
    
    
def modificar_proyecto(proyectos: dict):
    proyecto_id = ut.get_validar_int("Ingrese el ID del proyecto a modificar: ", 1)
    proyecto = next((p for p in proyectos if p["id"] == proyecto_id), None)
    
    if not proyecto:
        print("Proyecto no encontrado.")
        return

    while True:
        print("\n¿Qué desea modificar?")
        print("1. Nombre")
        print("2. Descripción")
        print("3. Presupuesto")
        print("4. Fecha de Inicio")
        print("5. Fecha de Fin")
        print("6. Estado")
        print("7. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            proyecto["Nombre del Proyecto"] = ut.get_validar_string("Nuevo Nombre (solo caracteres alfabéticos, máx 30): ", 30, alpha_only=True)
        elif opcion == '2':
            proyecto["Descripción"] = ut.get_validar_string("Nueva Descripción (alfanumérico, máx 200): ", 200)
        elif opcion == '3':
            proyecto["Presupuesto"] = ut.get_validar_int("Nuevo Presupuesto (mínimo $500000): ", 500000)
        elif opcion == '4':
            proyecto["Fecha de Inicio"] = ut.get_validar_date("Nueva Fecha de Inicio (DD/MM/AAAA): ").strftime("%d/%m/%Y")
        elif opcion == '5':
            proyecto["Fecha de Fin"] = ut.get_validar_date("Nueva Fecha de Fin (DD/MM/AAAA): ").strftime("%d/%m/%Y")
        elif opcion == '6':
            proyecto["Estado"] = ut.get_validar_string("Nuevo Estado (Activo, Cancelado, Finalizado): ", 9)
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
            
    print(f"Proyecto ID {proyecto_id} modificado exitosamente.")

def cancelar_proyecto(proyectos: list):
    id_a_eliminar = ut.get_validar_int("Ingrese el ID del proyecto a cancelar: ", 1)
    for proyecto in proyectos:
        if proyecto["id"] == id_a_eliminar:
            proyectos.remove(proyecto)
            print(f"Proyecto ID {id_a_eliminar} eliminado exitosamente.")
            return True 

    
        
    
    print(f"No se encontró ningún proyecto con ID {id_a_eliminar}.")
    return False  


    


def chequear_proyectos(proyectos: list):
    presente = datetime.datetime.now().date()
    
    for proyecto in proyectos:
        try:
            if "Fecha de Fin" in proyecto:
                fecha_fin_str = proyecto["Fecha de Fin"]
                try:
                    fecha_fin = datetime.datetime.strptime(fecha_fin_str, '%d-%m-%Y').date()
                except ValueError:
                    fecha_fin = datetime.datetime.strptime(fecha_fin_str, '%d/%m/%Y').date()
                
                if fecha_fin < presente and proyecto["Estado"] == "Activo":
                    proyecto["Estado"] = "Finalizado"
                    print(f"Proyecto '{proyecto['Nombre del Proyecto']}' ha sido finalizado.")
            else:
                print(f"Error: Falta la clave 'Fecha de Fin' en el proyecto {proyecto}")
        except KeyError as e:
            print(f"Error: Falta la clave {e} en el proyecto {proyecto}")
        except ValueError as e:
            print(f"Error al convertir la fecha en el proyecto {proyecto}: {e}")
            
def mostrar_proyectos(proyectos: list):
    print("-" * 174)
    print("| id |Nombre del Proyecto | Descripción | Presupuesto | Fecha de Inicio | Fecha de Fin | Estado |")
    for proyectos in proyectos:
        print("-" * 174)
        print(f"| {proyectos['id']}| {proyectos['Nombre del Proyecto']}| {proyectos['Descripción']} | ${proyectos['Presupuesto']} | {proyectos['Fecha de inicio']} | {proyectos['Fecha de Fin']} | {proyectos['Estado']} |")

def calcular_presupuesto_promedio(proyectos: list):
    total_presupuesto = 0
    for proyecto in proyectos:
        total_presupuesto += float(proyecto['Presupuesto'])
    
    presupuesto_promedio = total_presupuesto / len(proyectos)
    print(f"El presupuesto promedio es {presupuesto_promedio:.2f}")




def buscar_proyecto_nombre(proyectos: list):
    nombre = input("Ingrese el nombre del proyecto a buscar: ").lower()
    
    proyecto_encontrado = None
    for proyecto in proyectos:
        if proyecto["Nombre del Proyecto"].lower() == nombre:
            proyecto_encontrado = proyecto
            break
    
    if proyecto_encontrado:
        print("Proyecto encontrado:")
        print(proyecto_encontrado)
    else:
        print("Proyecto no encontrado.")
        
def ordenar_proyectos(proyectos: list):
    proyectos_original = copy.deepcopy(proyectos)
    while True:
        print("\n¿Ordenar por?")
        print("1. Nombre")
        print("2. Presupuesto")
        print("3. Fecha de Inicio")
        print("4. Volver al menú principal")
        
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            proyectos.sort(key=lambda x: x["Nombre del Proyecto"])
            mostrar_proyectos(proyectos)
        elif choice == '2':
            proyectos.sort(key=lambda x: x["Presupuesto"])
            mostrar_proyectos(proyectos)
        elif choice == '3':
            proyectos.sort(key=lambda x: datetime.datetime.strptime(x["Fecha de inicio"], "%d-%m-%Y"))
            mostrar_proyectos(proyectos)
        elif choice == '4':
            break
        else:
            print("Opción no válida. Intente de nuevo.")
        
        print("\nProyectos ordenados:")
        proyectos.clear()
        proyectos.extend(proyectos_original)   
            
def retomar_proyecto(proyectos):
    proyecto_id = ut.get_validar_int("Ingrese el ID del proyecto a retomar: ", 1)

    for proyecto in proyectos:
        if proyecto["id"] == proyecto_id and proyecto["Estado"] == "Cancelado":
            proyecto["Estado"] = "Activo"
            print(f"Proyecto ID {proyecto_id} retomado exitosamente.")
            return
    
    print("Proyecto no encontrado o no está cancelado.")
    

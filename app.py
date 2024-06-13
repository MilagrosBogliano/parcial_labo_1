import project_manager as pm
import archivos as fh
def Menu(proyectos):
    """
    La función `Menú` muestra un menú para gestionar proyectos y permite al usuario realizar varias
    acciones en una lista de proyectos.
    
    :param proyectos: Parece que el fragmento de código que proporcionaste es un sistema de menú para
    gestionar proyectos. La función `Menú` muestra un menú con varias opciones para gestionar proyectos
    y llama a diferentes funciones según la elección del usuario
    """
    while True:
        print("-" * 34)
        print("|Menú de Gestión de Proyectos:   |")
        print("|1. Ingresar proyecto            |")
        print("|2. Modificar proyecto           |")
        print("|3. Cancelar proyecto            |")
        print("|4. Comprobar proyectos          |")
        print("|5. Mostrar todos                |")
        print("|6. Calcular presupuesto promedio|")
        print("|7. Buscar proyecto por nombre   |")
        print("|8. Ordenar proyectos            |")
        print("|9. Retomar proyecto             |")
        print("|10. Salir                       |")
        print("-" * 34)
        choice = input("Seleccione una opción: ")
        
        if choice == '1':
            pm.Agregar_proyecto(proyectos)
        elif choice == '2':
            pm.modificar_proyecto(proyectos)
        elif choice == '3':
            pm.cancelar_proyecto(proyectos)
        elif choice == '4':
            pm.chequear_proyectos(proyectos)
        elif choice == '5':
            pm.mostrar_proyectos(proyectos)
        elif choice == '6':
            pm.calcular_presupuesto_promedio(proyectos)
        elif choice == '7':
            pm.buscar_proyecto_nombre(proyectos)
        elif choice == '8':
            pm.ordenar_proyectos(proyectos)
        elif choice == '9':
            pm.retomar_proyecto(proyectos)
        elif choice == '10':
            confirm = input("¿Está seguro que desea salir? (s/n): ").strip().lower()
            if confirm == 's':
                fh.guardar_proyectos_json(proyectos)
                fh.guardar_proyectos_csv(proyectos)
                print("Guardando proyectos y saliendo del programa...")
                break
            else:
                print("Opción no válida. Intente de nuevo.")

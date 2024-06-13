import project_manager as pm
from app import Menu
import archivos as fh



# Este fragmento de código es un modismo común de Python que verifica si el script actual se está
# ejecutando como programa principal.
if __name__ == "__main__":
     proyectos = fh.cargar_proyectos()
     Menu(proyectos)

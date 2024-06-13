import project_manager as pm
from app import Menu
import archivos as fh



if __name__ == "__main__":
     proyectos = fh.cargar_proyectos()
     Menu(proyectos)

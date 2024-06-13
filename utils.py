import re
import datetime

def get_validar_string(prompt, largo_maximo, alpha_only=False):
    while True:
        value = input(prompt)
        if len(value) > largo_maximo:
            print(f"El texto no puede exceder los {largo_maximo} caracteres.")
        elif alpha_only and not value.replace(" ", "").isalpha():  # Reemplazar espacios en blanco y verificar si solo contiene caracteres alfabéticos
            print("El texto solo puede contener caracteres alfabéticos.")
        else:
            return value.strip()  # Eliminar espacios en blanco alrededor del text

def get_validar_int(prompt, min_value):
    while True:
        try:
            value = int(input(prompt))
            if value < min_value:
                print(f"El valor debe ser mayor o igual a {min_value}.")
            else:
                return value
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

def get_validar_date(prompt, min_date=None):
    while True:
        date_str = input(prompt)
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            
            # Convertir min_date a datetime.datetime si es datetime.date
            if min_date and isinstance(min_date, datetime.date):
                min_date = datetime.datetime.combine(min_date, datetime.time.min)
            
            # Comparar date_obj con min_date
            if min_date and date_obj < min_date:
                print(f"La fecha debe ser posterior a {min_date.strftime('%d/%m/%Y')}.")
                continue
            
            return date_obj  # Devolver datetime.datetime
        except ValueError:
            print("Formato de fecha inválido. Por favor, ingrese la fecha en formato DD/MM/AAAA.")



import re
import datetime

def get_validar_string(prompt, largo_maximo, alpha_only=False):
    """
    La función `get_validar_string` solicita la entrada del usuario, valida la longitud y el contenido
    de la entrada y devuelve la entrada eliminada si cumple con los criterios especificados.
    
    :param prompt: El parámetro `prompt` es una cadena que se mostrará al usuario como un mensaje o
    pregunta, solicitándole que ingrese un valor. Sirve como guía o instrucción para el usuario sobre
    qué tipo de información se espera de él
    :param largo_maximo: El parámetro `largo_maximo` en la función `get_validar_string` representa la
    longitud máxima permitida para la cadena de entrada. La función solicitará al usuario que ingrese
    una cadena y, si la longitud de la cadena de entrada excede el `largo_maximo` especificado, mostrará
    un mensaje
    :param alpha_only: El parámetro `alpha_only` en la función `get_validar_string` es un indicador
    booleano que especifica si la cadena de entrada solo debe contener caracteres alfabéticos. Si
    `alpha_only` se establece en `True`, la función verificará si la cadena de entrada consta solo de
    caracteres alfabéticos (letras), defaults to False (optional)
    :return: La función `get_validar_string` devuelve el valor de entrada del usuario después de
    validarlo según las condiciones especificadas. Si la longitud de la entrada excede la longitud
    máxima especificada por `largo_maximo`, aparecerá un mensaje indicando que el texto no puede exceder
    la longitud especificada. Si `alpha_only` está configurado en `True` y la entrada contiene
    caracteres no alfabéticos (excluidos espacios),
    """
    while True:
        value = input(prompt)
        if len(value) > largo_maximo:
            print(f"El texto no puede exceder los {largo_maximo} caracteres.")
        elif alpha_only and not value.replace(" ", "").isalpha():  
            print("El texto solo puede contener caracteres alfabéticos.")
        else:
            return value.strip()  

def get_validar_int(prompt, min_value):
    """
    La función `get_validar_int` solicita al usuario que ingrese un valor entero mayor o igual a un
    valor mínimo especificado, manejando entradas no válidas y mostrando mensajes de error apropiados.
    
    :param prompt: El parámetro "prompt" es un mensaje o pregunta que se mostrará al usuario cuando se
    le solicite que ingrese un valor entero. Sirve como guía o instrucción para el usuario sobre qué
    tipo de información se espera de él
    :param min_value: El parámetro `min_value` en la función `get_validar_int` representa el valor
    mínimo al que la entrada del usuario debe ser mayor o igual para que se considere válida. Si el
    usuario ingresa un valor menor que `min_value`, se le pedirá que ingrese un valor que cumpla con los
    :return: La función `get_validar_int` devuelve un valor entero que ingresa el usuario después de
    validarlo para que sea mayor o igual al `min_value` especificado en los argumentos de la función. Si
    la entrada del usuario no es un número entero válido o es menor que "min_value", se muestran los
    mensajes de error apropiados y se le solicita al usuario que ingrese un número entero válido.
    """
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
    """
    La función `get_validar_date` solicita al usuario que ingrese una fecha en el formato DD/MM/AAAA,
    valida la entrada y garantiza que la fecha sea posterior a una fecha mínima especificada, si se
    proporciona.
    
    :param prompt: El parámetro `prompt` es una cadena que se mostrará al usuario cuando se le solicite
    que ingrese una fecha. Sirve como un mensaje o instrucción para guiar al usuario sobre qué
    información se espera de él
    :param min_date: El parámetro `min_date` en la función `get_validar_date` se utiliza para
    especificar la fecha mínima permitida para la entrada. Si se proporciona una "fecha_min" y el
    usuario ingresa una fecha anterior a la "fecha_min", la función le pedirá al usuario que ingrese una
    fecha que sea
    :return: La función `get_validar_date` devuelve un objeto de fecha y hora válido analizado a partir
    de la cadena de entrada del usuario si cumple con el formato especificado ("%d/%m/%Y") y cualquier
    requisito de fecha mínima. Si la fecha ingresada no es válida o no cumple con el requisito de fecha
    mínima, se muestran los mensajes de error apropiados y se solicita al usuario que ingrese una fecha
    válida.
    """
    while True:
        date_str = input(prompt)
        try:
            date_obj = datetime.datetime.strptime(date_str, "%d/%m/%Y")
            
            if min_date and isinstance(min_date, datetime.date):
                min_date = datetime.datetime.combine(min_date, datetime.time.min)
            
            if min_date and date_obj < min_date:
                print(f"La fecha debe ser posterior a {min_date.strftime('%d/%m/%Y')}.")
                continue
            
            return date_obj 
        except ValueError:
            print("Formato de fecha inválido. Por favor, ingrese la fecha en formato DD/MM/AAAA.")



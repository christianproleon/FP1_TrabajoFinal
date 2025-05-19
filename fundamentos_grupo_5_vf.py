# Importar librerías
import pandas
import os
from datetime import datetime

# Listas para almacenar los datos
lista_nombre = []
lista_fecha = []
lista_sexo = []
lista_edad = []
lista_peso = []
lista_talla = []
lista_presion = []
lista_frecuencia = []
lista_saturacion = []
lista_nivel = []
lista_imc = []
lista_clasificacion = []
lista_atencion = []

# Función para calcular el índice de masa corporal (IMC)
def calcular_imc(peso, talla_cm):
    talla_metro = talla_cm / 100
    return round(peso / (talla_metro ** 2), 2)

# Función para clasificar el IMC
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"
#=====================================================================
# GESTIÓN Y AUTOMATIZACIÓN DE REGISTROS DE PACIENTES EN POSTAS MÉDICAS
#=====================================================================
# - Renato Yassir Villafuerte Falcón
# - Christian Cordova Proleón
# - Alvaro Sebastian Nieva Salinas

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

# Función para clasificar la atención del paciente
def clasificar_atencion(edad, presion, frecuencia, saturacion, nivel_conciencia):
    if edad <= 75:
        if (presion < 90 or presion > 180 or
            frecuencia < 60 or frecuencia > 120 or
            saturacion < 92 or
            nivel_conciencia != "Alerta"):
            return "Urgente"
        else:
            return "Normal"
    else:
        if (presion < 100 or presion > 160 or
            frecuencia < 55 or frecuencia > 110 or
            saturacion < 94):
            return "Urgente"
        else:
            return "Normal"

#========================================
# Bucle para registrar datos del paciente
#========================================
while True:
    print("\n====== Registrar datos del Paciente ======")

    # Registrar nombres del paciente
    while True:
        nombre = input("Nombre y apellido: ").strip().upper()
        if nombre != "":
            break
        print("❗Error: Ingrese nombres del paciente")

    # Registrar fecha de atención
    fecha = datetime.now().strftime('%d-%m-%Y %H:%M')

    # Registrar y validar el sexo
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M","F"]:
            if sexo == "M":
                sexo = "Masculino"
            else:
                sexo = "Femenino"
            break
        else:
            print("❗Error: Ingrese 'M' (Masculino) o 'F' (Femenino)")

    # Registrar y validar la edad
    while True:
        try:
            edad = int(input("Edad (años): "))
            if 0 < edad <= 100:
                break
            else:
                print("❗Error: Ingrese una edad válida")
        except ValueError:
            print("❗Error: Ingrese un número entero")

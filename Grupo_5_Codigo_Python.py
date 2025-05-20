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
from tabulate import tabulate
from zoneinfo import ZoneInfo

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
    if edad <= 60 or imc <= 25:
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
    horaLima = ZoneInfo("America/Lima")
    fecha = datetime.now(horaLima).strftime('%d-%m-%Y %H:%M')

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

    # Registrar y validar el peso
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if 0 < peso <= 120:
                break
            else:
                print("❗Error: Ingrese un peso válido")
        except ValueError:
            print("❗Error: Ingrese un número real")

    # Registrar y validar la talla
    while True:
        try:
            talla_cm = float(input("Talla (centímetros): "))
            if 0 < talla_cm <= 210:
                break
            else:
                print("❗Error: Ingrese una talla válida")
        except ValueError:
            print("❗Error: Ingrese un número real")

    # Registrar y validar la presión sistólica
    while True:
        try:
            presion = float(input("Presión sistólica (mmHg): "))
            if 0 < presion <= 250:
                break
            else:
                print("❗Error: Ingrese presión sistólica válida")
        except ValueError:
                print("❗Error: Ingrese un número real")

    # Registrar y validar la frecuencia cardiaca
    while True:
        try:
            frecuencia = int(input("Frecuencia cardiaca (lpm): "))
            if 0 < frecuencia <= 250:
                break
            else:
                print("❗Error: Ingrese frecuencia cardiaca válida")
        except ValueError:
                print("❗Error: Ingrese un número entero")

    # Registrar y validar la saturación de oxígeno
    while True:
        try:
            saturacion = int(input("Saturación de oxígeno (%): "))
            if 50 < saturacion <= 100:
                break
            else:
                print("❗Error: Ingrese saturación de oxígeno válida")
        except ValueError:
                print("❗Error: Ingrese un número entero")

    # Registrar y validar el nivel de conciencia
    while True:
        nivel_conciencia = input("Nivel de conciencia (A/V/D/I): ").strip().upper()
        if nivel_conciencia in ["A","V","D","I"]:
            if nivel_conciencia == "A":
                nivel_conciencia = "Alerta"
            elif nivel_conciencia == "V":
                nivel_conciencia = "Verbal"
            elif nivel_conciencia == "D":
                nivel_conciencia = "Dolor"
            else:
                nivel_conciencia = "Inconsciente"
            break
        else:
            print("❗Error: Ingrese solo 'A','V','D' o 'I'")

    # Calcular y clasificar el IMC
    imc = calcular_imc(peso, talla_cm)
    clasificacion = clasificar_imc(imc)

    # Clasificar la atención del paciente
    atencion = clasificar_atencion(edad, presion, frecuencia, saturacion, nivel_conciencia)

    # Mostrar reporte inmediato del paciente
    print(f"\n👨‍⚕️📝 Reporte del paciente '{nombre}'")
    print(f"Fecha de atención: {fecha}")
    print(f"Sexo: {sexo}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Talla: {talla_cm} cm")
    print(f"Presión sistólica: {presion} mmHg")
    print(f"Frecuencia cardiaca: {frecuencia} lpm")
    print(f"Saturación de oxígeno: {saturacion} %")
    print(f"Nivel de conciencia: {nivel_conciencia}")
    print(f"IMC: {imc} ({clasificacion})")
    print(f"Prioridad de atención: {atencion}")
    print("==========================================")

    # Guardar los datos en listas
    lista_nombre.append(nombre)
    lista_fecha.append(fecha)
    lista_sexo.append(sexo)
    lista_edad.append(edad)
    lista_peso.append(peso)
    lista_talla.append(talla_cm)
    lista_presion.append(presion)
    lista_frecuencia.append(frecuencia)
    lista_saturacion.append(saturacion)
    lista_nivel.append(nivel_conciencia)
    lista_imc.append(imc)
    lista_clasificacion.append(clasificacion)
    lista_atencion.append(atencion)

    # Preguntar si se desea continuar registrando
    while True:
        continuar = input("\n¿Desea registrar otro paciente? (S/N): ").strip().upper()
        if continuar in ('S','N'):
            break
        else:
            print("❗Error: Por favor, ingrese 'S' para Sí o 'N' para No")
    if continuar == 'N':
        break

#=====================================
# Reporte final de todos los pacientes
#=====================================
# Encabezado
print(f"\n★★★★★★★★★★★★★★★★★★★★ Reporte final de los {len(lista_nombre)} pacientes ★★★★★★★★★★★★★★★★★★★★")

# Crear tabla de datos
tabla_datos = []
for i in range(0,len(lista_nombre),1):
    tabla_datos.append([
        i+1,
        lista_nombre[i],
        lista_fecha[i],
        lista_sexo[i],
        lista_edad[i],
        lista_peso[i],
        lista_talla[i],
        lista_presion[i],
        lista_frecuencia[i],
        lista_saturacion[i],
        lista_nivel[i],
        lista_imc[i],
        lista_clasificacion[i],
        lista_atencion[i]
    ])

columnas = ["N°", "Nombre y apellido", "Fecha de atención", "Sexo", "Edad\n(años)", "Peso\n(kg)", "Talla\n(cm)", "Presión\nsistólica", "Frecuencia\ncardiaca (lpm)",
            "Saturación de\noxígeno (%)", "Nivel de\nconciencia", "IMC", "Clasificación\nIMC", "Nivel de\natención"]
tabla_datos = pandas.DataFrame(tabla_datos, columns=columnas)

# Imprimir tabla de datos
print(tabulate(tabla_datos, headers=columnas, tablefmt="fancy_grid", showindex=False))

# Guardar reporte final en Excel
archivo = "reporte_final_pacientes_" + datetime.now().strftime('%d-%m-%Y') + ".xlsx"
tabla_datos.to_excel(archivo, index=False)
print(f"\nReporte final guardado en la carpeta: \n{os.getcwd() + "\\" + archivo}")

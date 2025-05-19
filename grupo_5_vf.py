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
print(f"{'':<3} {'':<25} {'':<18} {'':<10} {'':<5} {'':<5} {'':<6} {'Presión':<10} {'Frecuencia':<11} {'Saturación':<11} {'Nivel de':<11} {'':<5} {'Clasificar':<11} {'Nivel de'}")
print(f"{'N°':<3} {'Nombre y apellido':<25} {'Fecha de atención':<18} {'Sexo':<10} {'Edad':<5} {'Peso':<5} {'Talla':<6} {'sistólica':<10} {'cardiaca':<11} {'de oxígeno':<11} {'conciencia':<11} {'IMC':<5} {'IMC':<11} {'atención'}")
print("-" * 155)

# Filas de datos
for i in range(len(lista_nombre)):
    print(f"{i + 1:<3} {lista_nombre[i]:<25} {lista_fecha[i]:<18} {lista_sexo[i]:<10} {lista_edad[i]:<5} {lista_peso[i]:<5.1f} {lista_talla[i]:<6.1f} {lista_presion[i]:<10.1f} {lista_frecuencia[i]:<11} {lista_saturacion[i]:<11} {lista_nivel[i]:<11} {lista_imc[i]:<5.1f} {lista_clasificacion[i]:<11} {lista_atencion[i]}")
print("-" * 155)

# Crear tabla de datos
datos = pandas.DataFrame({
    "nombres": lista_nombre,
    "fecha_atencion": lista_fecha,
    "sexo": lista_sexo,
    "edad": lista_edad,
    "peso": lista_peso,
    "talla": lista_talla,
    "presion_sistolica": lista_presion,
    "frecuencia_cardiaca": lista_frecuencia,
    "saturacion_oxígeno": lista_saturacion,
    "nivel_conciencia": lista_nivel,
    "imc": lista_imc,
    "clasificacion_imc": lista_clasificacion,
    "prioridad_atencion": lista_atencion
})

# Guardar reporte final en Excel
archivo = "reporte_final_pacientes_" + datetime.now().strftime('%d-%m-%Y') + ".xlsx"
datos.to_excel(archivo, index=False)
print(f"\nReporte final guardado en la carpeta: \n{os.getcwd() + "\\" + archivo}")

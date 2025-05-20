from datetime import datetime
from zoneinfo import ZoneInfo  
from tabulate import tabulate  # Es necesario tener instalada esta librería

# Listas para almacenar los datos
lista_nombre = []
lista_fecha = []
lista_sexo = []
lista_edad = []
lista_peso = []
lista_talla = []
lista_imc = []
lista_clasificacion = []
lista_presion = []
lista_frecuencia = []
lista_saturacion = []
lista_nivel = []
lista_atencion = []

# Contador para el nivel de urgencia
nivel_de_atencion = 0

# Función que clasifica el nivel de la prioridad de atención según el valor del contador
def urgencia(nivel_de_atencion):
    nivel_de_urgencia = None
    
    if nivel_de_atencion == 0:
        nivel_de_urgencia = "Normal"
        
    elif nivel_de_atencion == 1:
        nivel_de_urgencia = "1 (Urgencia)"
        
    elif nivel_de_atencion == 2:
        nivel_de_urgencia = "2 (Urgencia)"
        
    elif nivel_de_atencion == 3:
        nivel_de_urgencia = "3 (Urgencia)"
        
    else:
        nivel_de_urgencia = "4 (Urgencia crítica)"
    
    return nivel_de_urgencia

# Funciones auxiliares
def calcular_imc(peso, talla_cm):
    talla_m = talla_cm / 100
    return round(peso / (talla_m ** 2), 2)

# Función que calcula el Índice de Masa Corporal
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:40
        return "Obesidad"

# Función que calcula el nivel de atención según los datos ingresados
# El grupo de rangos estables se determina a partir de los valores de la edad y el IMC
def clasificar_atencion(edad, imc, presion, frecuencia, saturacion, nivel_conciencia, nivel_de_atencion):
    
    # Cálculo para paciente común
    if (edad <= 60 or imc <= 25):
            if (presion < 90 or presion > 180):
                nivel_de_atencion += 1
                
            if (frecuencia < 60 or frecuencia > 120):
                nivel_de_atencion += 1
                
            if (saturacion < 92):
                nivel_de_atencion += 1
                
            if (nivel_conciencia != "En Alerta"):
                nivel_de_atencion += 1
                
            #Si el paciente está inconciente se vuelve prioridad máxima independientemente de las otras variables.    
            if (nivel_conciencia == "Inconsciente"):
                nivel_de_atencion = 4
                
    # Cálculo para paciente mayor de edad o con sobrepeso
    else:
            if (presion < 100 or presion > 160):
                nivel_de_atencion += 1
                
            if (frecuencia < 55 or frecuencia > 110):
                nivel_de_atencion += 1
                
            if (saturacion < 94):
                nivel_de_atencion += 1
                
            if (nivel_conciencia != "En Alerta"):
                nivel_de_atencion += 1
            
            #Si el paciente está inconciente se vuelve prioridad máxima independientemente de las otras variables.
            if (nivel_conciencia == "Inconsciente"):
                nivel_de_atencion = 4    
                
    return urgencia(nivel_de_atencion)

# Bucle principal
while True:
    print("\n====== Registrar datos del Paciente ======")

    # Datos personales
    while True:
        nombre = input("Nombre y apellido: ").strip().upper()
        if nombre:
            break
        print("❗Error: Ingrese nombres del paciente")
    # Fecha de registro con el huso horario de Lima, Perú
    horaLima = ZoneInfo("America/Lima")
    fecha = datetime.now(horaLima).strftime('%d-%m-%Y %H:%M')
    
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            sexo = "Masculino" if sexo == "M" else "Femenino"
            break
        print("❗Error: Ingrese 'M' o 'F'")

    while True:
        try:
            edad = int(input("Edad (años): "))
            if 0 < edad <= 100:
                break
            print("❗Error: Edad inválida")
        except ValueError:
            print("❗Error: Ingrese un número entero")

    while True:
        try:
            peso = float(input("Peso (kg): "))
            if 0 < peso <= 200:
                break
            print("❗Error: Peso inválido")
        except ValueError:
            print("❗Error: Ingrese un número válido")

    while True:
        try:
            talla = float(input("Talla (cm): "))
            if 0 < talla <= 210:
                break
            print("❗Error: Talla inválida")
        except ValueError:
            print("❗Error: Ingrese un número válido")

    # Signos vitales
    while True:
        try:
            presion = float(input("Presión sistólica (mmHg): "))
            if 0 < presion <= 250:
                break
            print("❗Error: Presión inválida")
        except ValueError:
            print("❗Error: Ingrese un número válido")

    while True:
        try:
            frecuencia = int(input("Frecuencia cardíaca (lpm): "))
            if 0 < frecuencia <= 240:
                break
            print("❗Error: Frecuencia inválida")
        except ValueError:
            print("❗Error: Ingrese un número válido")

    while True:
        try:
            saturacion = int(input("Saturación de oxígeno (%): "))
            if 50 < saturacion <= 100:
                break
            print("❗Error: Saturación inválida")
        except ValueError:
            print("❗Error: Ingrese un número válido")

    while True:
        nivel = input("Nivel de conciencia (A/V/D/I): ").strip().upper()
        if nivel in ["A", "V", "D", "I"]:
            nivel_conciencia = {
                "A": "En Alerta",
                "V": "Verbal",
                "D": "Dolor",
                "I": "Inconsciente"
            }[nivel]
            break
        print("❗Error: Ingrese A, V, D o I")

    # Cálculos
    imc = calcular_imc(peso, talla)
    clasificacion = clasificar_imc(imc)
    atencion = clasificar_atencion(edad, imc, presion, frecuencia, saturacion, nivel_conciencia, nivel_de_atencion)

    # Mostrar resumen
    print(f"\n👨‍⚕️📝 Reporte del paciente '{nombre}'")
    print(f"Fecha: {fecha}")
    print(f"Sexo: {sexo}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Talla: {talla} cm")
    print(f"Presión: {presion} mmHg")
    print(f"Frecuencia cardiaca: {frecuencia} lpm")
    print(f"Saturación de oxígeno: {saturacion} %")
    print(f"IMC: {imc} ({clasificacion})")
    print(f"Nivel de conciencia: {nivel_conciencia}")
    print("")
    print(f"Prioridad de atención: {atencion}")

    # Guardar datos
    lista_nombre.append(nombre)
    lista_fecha.append(fecha)
    lista_sexo.append(sexo)
    lista_edad.append(edad)
    lista_peso.append(peso)
    lista_talla.append(talla)
    lista_imc.append(imc)
    lista_clasificacion.append(clasificacion)
    lista_presion.append(presion)
    lista_frecuencia.append(frecuencia)
    lista_saturacion.append(saturacion)
    lista_nivel.append(nivel_conciencia)
    lista_atencion.append(atencion)

    # Continuar
    continuar = input("\n¿Registrar otro paciente? (S/N): ").strip().upper()
    if continuar != 'S':
        break
    
# Reporte Final tabular
print("\n===== Reporte Final de Pacientes =====\n")

datos_tabla = []
for i in range(len(lista_nombre)):
    datos_tabla.append([
        i+1,
        lista_nombre[i],
        lista_fecha[i],
        lista_sexo[i],
        lista_edad[i],
        lista_peso[i],
        lista_talla[i],
        lista_imc[i],
        lista_clasificacion[i],
        lista_presion[i],
        lista_frecuencia[i],
        lista_saturacion[i],
        lista_nivel[i],
        lista_atencion[i]
    ])

columnas = ["#", "Nombre", "Fecha", "Sexo", "Edad", "Peso", "Talla", "IMC", "Clasificación",
            "Presión", "Frecuencia cardiaca", "Saturación de oxígeno", "Nivel de conciencia", "Prioridad de atención"]

print(tabulate(datos_tabla, headers=columnas, tablefmt="grid"))

from datetime import datetime

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

# Funciones auxiliares
def calcular_imc(peso, talla_cm):
    talla_m = talla_cm / 100
    return round(peso / (talla_m ** 2), 2)

def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

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

# Bucle principal
while True:
    print("\n====== Registrar datos del Paciente ======")

    # Datos personales
    while True:
        nombre = input("Nombre y apellido: ").strip().upper()
        if nombre:
            break
        print("❗Error: Ingrese nombres del paciente")
    fecha = datetime.now().strftime('%d-%m-%Y %H:%M')

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
            if 0 < peso <= 120:
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
            if 0 < frecuencia <= 250:
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
                "A": "Alerta",
                "V": "Verbal",
                "D": "Dolor",
                "I": "Inconsciente"
            }[nivel]
            break
        print("❗Error: Ingrese A, V, D o I")

    # Cálculos
    imc = calcular_imc(peso, talla)
    clasificacion = clasificar_imc(imc)
    atencion = clasificar_atencion(edad, presion, frecuencia, saturacion, nivel_conciencia)

    # Mostrar resumen
    print(f"\n👨‍⚕️📝 Reporte del paciente '{nombre}'")
    print(f"Fecha: {fecha}")
    print(f"Sexo: {sexo}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Talla: {talla} cm")
    print(f"Presión: {presion} mmHg")
    print(f"Frecuencia: {frecuencia} lpm")
    print(f"Saturación: {saturacion} %")
    print(f"Nivel de conciencia: {nivel_conciencia}")
    print(f"IMC: {imc} ({clasificacion})")
    print(f"Nivel de atención: {atencion}")

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

# Reporte Final
print("\n===== Reporte Final de Pacientes =====")
for i in range(len(lista_nombre)):
    print(f"{i+1}. {lista_nombre[i]} | IMC: {lista_imc[i]} ({lista_clasificacion[i]}) | Atención: {lista_atencion[i]}")

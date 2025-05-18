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

# Función para calcular IMC
def calcular_imc(peso, talla_cm):
    talla_m = talla_cm / 100
    return round(peso / (talla_m ** 2), 2)

# Función para clasificar IMC
def clasificar_imc(imc):
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

# Bucle para registrar datos del paciente
while True:
    print("\n====== Registrar datos del Paciente ======")

    # Nombre y fecha
    while True:
        nombre = input("Nombre y apellido: ").strip().upper()
        if nombre:
            break
        print("❗Error: Ingrese nombres del paciente")

    fecha = datetime.now().strftime('%d-%m-%Y %H:%M')

    # Sexo
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            sexo = "Masculino" if sexo == "M" else "Femenino"
            break
        print("❗Error: Ingrese 'M' o 'F'")

    # Edad
    while True:
        try:
            edad = int(input("Edad (años): "))
            if 0 < edad <= 100:
                break
            print("❗Error: Ingrese una edad válida")
        except ValueError:
            print("❗Error: Ingrese un número entero")

    # Peso
    while True:
        try:
            peso = float(input("Peso (kg): "))
            if 0 < peso <= 120:
                break
            print("❗Error: Ingrese un peso válido")
        except ValueError:
            print("❗Error: Ingrese un número real")

    # Talla
    while True:
        try:
            talla = float(input("Talla (cm): "))
            if 0 < talla <= 210:
                break
            print("❗Error: Ingrese una talla válida")
        except ValueError:
            print("❗Error: Ingrese un número real")

    # Calcular y clasificar IMC
    imc = calcular_imc(peso, talla)
    clasificacion = clasificar_imc(imc)

    # Mostrar resumen
    print(f"\n👨‍⚕️📝 Datos registrados del paciente '{nombre}'")
    print(f"Fecha: {fecha}")
    print(f"Sexo: {sexo}")
    print(f"Edad: {edad} años")
    print(f"Peso: {peso} kg")
    print(f"Talla: {talla} cm")
    print(f"IMC: {imc} ({clasificacion})")

    # Guardar datos
    lista_nombre.append(nombre)
    lista_fecha.append(fecha)
    lista_sexo.append(sexo)
    lista_edad.append(edad)
    lista_peso.append(peso)
    lista_talla.append(talla)
    lista_imc.append(imc)
    lista_clasificacion.append(clasificacion)

    # Continuar
    continuar = input("\n¿Registrar otro paciente? (S/N): ").strip().upper()
    if continuar != 'S':
        break

# Reporte final
print("\n===== Reporte Final =====")
for i in range(len(lista_nombre)):
    print(f"{i+1}. {lista_nombre[i]} | {lista_fecha[i]} | {lista_sexo[i]} | Edad: {lista_edad[i]} | Peso: {lista_peso[i]} kg | Talla: {lista_talla[i]} cm | IMC: {lista_imc[i]} ({lista_clasificacion[i]})")

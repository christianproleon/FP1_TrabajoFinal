from datetime import datetime

# Listas para almacenar los datos
lista_nombre = []
lista_fecha = []
lista_sexo = []

# Bucle para registrar datos del paciente
while True:
    print("\n====== Registrar datos del Paciente ======")

    # Registrar nombres del paciente
    while True:
        nombre = input("Nombre y apellido: ").strip().upper()
        if nombre != "":
            break
        print("❗Error: Ingrese nombres del paciente")

    # Fecha de atención
    fecha = datetime.now().strftime('%d-%m-%Y %H:%M')

    # Registrar sexo
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            sexo = "Masculino" if sexo == "M" else "Femenino"
            break
        print("❗Error: Ingrese 'M' o 'F'")

    # Mostrar datos registrados
    print(f"\n👨‍⚕️📝 Datos registrados")
    print(f"Nombre: {nombre}")
    print(f"Fecha: {fecha}")
    print(f"Sexo: {sexo}")

    # Guardar en listas
    lista_nombre.append(nombre)
    lista_fecha.append(fecha)
    lista_sexo.append(sexo)

    # Continuar o salir
    continuar = input("\n¿Registrar otro paciente? (S/N): ").strip().upper()
    if continuar != 'S':
        break

# Mostrar reporte final
print("\n===== Reporte Final =====")
for i in range(len(lista_nombre)):
    print(f"{i+1}. {lista_nombre[i]} - {lista_fecha[i]} - {lista_sexo[i]}")

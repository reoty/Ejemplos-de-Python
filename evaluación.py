
# Función para calcular el costo total basado en el plan y la duración
def calcular_costo(plan, cliente_nuevo):
    # Definir los precios base de cada plan
    precios = {
        "mensual": 10000,
        "trimestral": 20000,
        "anual": 100000
    }

    # Obtener el precio base del plan seleccionado
    precio_base = precios[plan]
    
    # Calcular el costo total con descuento basado en si es cliente nuevo o no
    if cliente_nuevo:
        descuento = precio_base * 0.1  # 10% de descuento para clientes nuevos
    else:
        descuento = precio_base * 0.2  # 20% de descuento para clientes existentes
    
    costo_total = precio_base - descuento
    return precio_base, descuento, costo_total

# Pedido de datos relevantes
nombre = input("Ingrese su nombre: ")
correo = input("Ingrese su correo electrónico: ")
edad = input("Ingrese su edad: ")

# Pequeño ciclo para saber si es cliente nuevo
while True:
    pregunta = input("¿Cliente nuevo? si/no: ").lower()
    if pregunta == "si":
        cliente_nuevo = True
        break
    elif pregunta == "no":
        cliente_nuevo = False
        break
    else:
        print("Por favor seleccione si o no...")

# Bucle para asegurar que el usuario seleccione una opción válida de plan
while True:
    print("Seleccione su plan de suscripción: \n 1. Plan Mensual: $10000 \n 2. Plan Trimestral: $20000 \n 3. Plan Anual: $100000")
    opcion = input("Ingrese el número de su opción: ")
    
    if opcion == "1":
        plan = "mensual"
        duracion = "1 mes"
        break
    elif opcion == "2":
        plan = "trimestral"
        duracion = "3 meses"
        break
    elif opcion == "3":
        plan = "anual"
        duracion = "12 meses"
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")

# Calcular los costos usando la función creada
precio_base, descuento, costo_total = calcular_costo(plan, cliente_nuevo)

# Mostrar la información al usuario
print("\n--- Resumen de Inscripción ---")
print(f"Nombre: {nombre}")
print(f"Correo electrónico: {correo}")
print(f"Edad: {edad} años")
print(f"Plan seleccionado: {plan.capitalize()}")
print(f"Duración de la inscripción: {duracion}")
print(f"Costo total antes del descuento: ${precio_base}")
print(f"Descuento aplicado: ${descuento}")
print(f"Costo total después del descuento: ${costo_total}")

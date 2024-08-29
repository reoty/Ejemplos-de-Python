# Definición de la función para calcular el costo total de forma alternativa a la planteada en clases.
def calcular_costo_total(plan, meses):
    precios = {
        "Básico": 1000,
        "Estándar": 1500,
        "Premium": 2000
    }
    return precios[plan] * meses #Entendiendo como funciona el return podemos hacer que el retorno sea el cálculo en si que necesitamos.
# Solicitar el nombre del usuario
nombre = input("Ingrese su nombre: ")
# Solicitar el correo electrónico del usuario
correo = input("Ingrese su correo electrónico: ")
# Solicitar la selección del plan de suscripción
print("Seleccione su plan de suscripción: \n 1. Plan Básico: $1000/mes \n 2. Plan Estándar: $1500/mes \n 3. Plan Premium: $2000/mes")
#me gusta hacerlo asi :v
opcion = input("Ingrese el número de su opción: ")

if opcion == "1": #El retorno va a multiplicar  los meses asi que podemos crear if más cortos.
    plan = "Básico"
elif opcion == "2":
    plan = "Estándar"
elif opcion == "3":
    plan = "Premium"
else:
    print("Opción no válida")
# Solicitar la duración de la suscripción en meses
meses = int(input("Ingrese la duración de la suscripción en meses: ")) #aquí le damos el valor al retorno.
# Calcular el costo total utilizando la función
costo_total = calcular_costo_total(plan, meses)
# Generar el reporte
reporte = f"""
Reporte de Suscripción
-----------------------
Nombre del Usuario: {nombre}
Correo Electrónico: {correo}
Plan Seleccionado: {plan}
Duración de la Suscripción: {meses} meses
Costo Total: ${costo_total}
"""

print(reporte) #descubrí que se podía hacer esto (sirve bastante en bases de datos, también se puede reciclar texto o crear funciones con ṕalabras, lo que se te ocurra.)

#cosas para aprender python
#Python no le importa mucho como hagas las cosas, pero si es delicado con la identación jaja, algo que no importa mucho en otros lenguajes, aquí importa demasiado.
#uso de print y cadena de carácteres
print('hola mundo')
#declarando variables, detecta si es entero o decimal tan solo si lleva o no punto,
a = 25
b = 25.2
b1 = 2
#suma (la resta y demás son los otros operadores - * /)
c = a+b
#potencia ^
d = a**b
#resto de una división
e = a%b
#cadena de caracter
f = 'hola'
#convirtiendo entero a cadena para visualizar y concatenar (irrelevante pero se puede)
print(str(a) + ' ' + str(b))
#lo mismo de arriba, se crean solo los espacios, permite cualquier variable, \n da un salto de linea,
print('\n' ,a, '\n', b, '\na+b\n', c, '\n esta es la d\n', d, '\n', e, '\n', f,'\n', b1)
#lo mismo, pero con fstring
print(f"{a} {b}")
#se puede hacer esto sin necesidad de for ni nada, muestra el hola repetido la cantidad de veces que pongas.
print('hola\n'*3)
# Varias formas de devolver, no se puede multiplicar texto por otra variable.
print('\na\n'*6)
#listas
lista = [1,4,5,6]
type(lista)
print(lista)
lista2 = [1,2,3,4]
type(tuple) #identifica que es lista
print(lista2)
#muestra el valor ubicado en la posición de la lista, empieza por 0
print(lista[0], lista[3], lista2[2])
lista3 = [7,8,9,10]
print(lista3)
#borra lo que este en la posición 2
lista3.pop(2)
print(lista3)
#cambia la posición 1
lista3[1]=15
print(lista3)
print(lista3[2])
#agrega al final de la lista el 12, en nueva posición
lista3.append(12)
print(lista3)
lista4 =[4,12,19,14,2,5]
print(lista4)
lista4.sort()
#ordena la lista
print(lista4)
lista5 = [5,5,2,6,1,3,6,5]
#cuenta la cantidad de veces que se repite lo indicado.
output = lista5.count(5)
print(lista5)
print(output)
print(lista, 'y', lista3)
#Extiende la lista con lo de la otra.
lista.extend(lista3)
print(lista)
#la ubicación del indice de lo encerrado en ()
vista= lista.index(15)
print(vista)
#da la vuelta :V
lista.reverse()
print(lista)
#inserta en la posición del indive en el primero, el valor a insertar, desplaza los demás.
lista.insert(3,55)
print(lista)
#remueve el valor indicado,
lista.remove(55)
print(lista)
#copia lo de la lista indicada en la lista nueva
lista6 = lista.copy()
print('', lista, '\n', lista6)
#crea una lista a partir del rango de índice.
sublista = lista[0:4]
print(sublista)
#Valores booleanos, se pueden escribir naturalmente o implícito en ifs y todo eso.
x = True
y = False
print(x and y)
print(x or y)
print(not x, not y)
#otros valores porque si :V , uso de > < and or not
a = 5
b = 10
c = 15
# Verifica si 'a' es menor que 'b' y 'b' es menor que 'c'
if a < b and b < c:
    #mira aquí como la identación es oblogatoria, es la forma que Python lee las cosas en carencia de ; {} y demas cosas.
    print("a es menor que b y b es menor que c")
elif a > b and c:
    #para continuaar con if usamos elif
    print("Es diferente la cosa")
else:
    print("La condición no se cumple")
# Verifica si 'a' es mayor que 'b' o 'b' es mayor que 'c'
if a > b or b > c:
    print("a es mayor que b o b es mayor que c")
else:
    print("La condición no se cumple 2")
# Verifica si 'a' no es igual a 10
if not a == 10:
    print("a no es igual a 10")
else:
    print("La condición no se cumple 3")
# Objetos, representan la realidad con sus clases y propiedades.
class perro:
    ladrar = "guau"
    aullar = "auuu"
#Si asgnas objetos a una variable se comporta comom ese objeto
objeto = perro
print(objeto)
#Se llama a la propiedad asi.
objeto = perro.ladrar
print(objeto)
#Se puede llamar a la propiedad de forma directa si se necesita.
print(perro.aullar)
#se puede llamar a la propiedad desde la variable asignada
objeto = perro
print(objeto.ladrar)
#podemos modificar la propiedad del objeto.
perro.ladrar = "wof"
print(perro.ladrar)
perro.ladrar = "guau"
#podemos agregar propiedades al objeto.
perro.ladrar_ingles = "woof"
perro.ladrar_frances = "wuof"
print(perro.ladrar, perro.ladrar_ingles, perro.ladrar_frances, perro.aullar)
#Una utilidad de las clases es creales métodos e invocar sus funcionalidades más adelante, cuantas veces se quiera.
class Operaciones:
    @staticmethod
    def sumar(x, y):
        return x + y
    @staticmethod
    def restar(x, y):
        return x - y
    @staticmethod
    def multiplicar(x, y):
        return x * y
    @staticmethod
    def dividir(x, y):
    #Para evitarse problemas, siempre es bueno usar un if que evite dividir por cero, intenta hacerlo jaja
        if y != 0:
            return x / y
        else:
            return "No se puede dividir por cero"
# En Python, el decorador @staticmethod se utiliza para definir métodos estáticos.
# Un método estático no tiene acceso a la instancia de la clase y no necesita la palabra clave 'self'.
# Por lo tanto, los métodos estáticos se pueden llamar directamente desde la clase sin crear una instancia de la misma.
print(Operaciones.sumar(5, 5))
print(Operaciones.restar(5, 5))
print(Operaciones.multiplicar(5, 5))
print(Operaciones.dividir(5, 5))
print(Operaciones.dividir(5, 0))
#ejemplo básico de calculadora.
x=int(input("Ingrese el primer número: \n > ")) #podemos indicar al usuario que ingresar desde una misma linea.
y=int(input("Ingrese el segundo número \n >"))
op=input("Ingrese alguna opción \n (1.) Sumar \n (2.) Restar \n (3.) Multiplicar \n (4.) Dividir \n >")
#se aplica el if
if op == "1":
    print(Operaciones.sumar(x,y)) #aqui solo identificamos las variables porque ya le pedimos los datos al usuario antes,
elif op == "2":
    print(Operaciones.restar(x,y))
elif op == "3":
    print(Operaciones.multiplicar(x,y))
elif op == "4":
    print(Operaciones.dividir(x,y))
else:
    print("Opción incorrecta")
input("Enter para continuar...") #una pausa que continua con enter de parte del usuario.
#En caso de no usar @staticmethod será necesario declarra una instancia que es lo que Python espera, si no se hace dará error.
#usamos Self para que python espere esa instancia.
class Operaciones2:
    #este def está definiendo una nueva función, veremos eso un poquito más abajo.
    def sumar(self, x, y):
        return x + y
    def restar(self, x, y):
        return x - y
    def multiplicar(self, x, y):
        return x * y
    def dividir(self, x, y):
        if y != 0:
            return x / y
        else:
            return "No se puede dividir por cero"
# Para usar estos métodos, necesitarías crear una instancia de la clase Operaciones2
operaciones_instancia = Operaciones2()
# Llamadas a los métodos usando la instancia creada
print(operaciones_instancia.sumar(5, 5))
print(operaciones_instancia.restar(10, 5))
print(operaciones_instancia.multiplicar(2, 3))
print(operaciones_instancia.dividir(10, 2))
print(operaciones_instancia.dividir(10, 0))
#También existen funciones directas si se quiere por ejemplo sumar, restar u otras operaciones.
print(sum([2,2,2,]))
#se puede usaar directo o invocar una lista
lis = [4,3,2,5]
#suma, valor máximo, valor mínimo, longitud de lista, ordenar lusta, valor absoluto, (número, elevado a la potencia), redondeo,
print(sum(lis), max(lis), min(lis), len(lis), sorted(lis), abs(-5), pow(2,2), round(3.1415162,2)) #Y muchos, muchos más :v
#estas funciones vienen integradas, pero podemos hacer las nuestras propias. hagamos una que devuelva un booleano de si es o no par un número.
def espar(numero):
    return numero % 2==0 #se entiende que si el resto de dividir numero da 0 es true, si no da 0 es false.
print(espar(5), espar(12))
#modifiquemos un poco la función para que acepte el uso de listas.
def espar_lista(listas):
    return [numero % 2==0 for numero in listas] #lo mismo, pero por cada numero en una lista
print(espar_lista(lis)) #Ya ahora solo es cosa de aprender bien esto y ser creativos.
#por ejemplo, mejoramos lo recién creado para que diga en pantalla, par o inpar asi.
def espar2(numero):
    if numero % 2==0: #se entiende que si el resto de dividir numero da 0 es true, si no da 0 es false.
        return "par" #pero si es true retorna par,
    else:
        return "impar" #si no es true, o sea false, retorna impar
def espar_lista2(lista):
    #ojo aquí, no hay identación
    return ["par" if numero % 2==0 else "impar" for numero in lista] #lo mismo, por cada numero de lista
print(espar2(9), espar2(8), '\n', espar_lista2(lis))
print(espar(2), espar2(2))
#se pueden meter funciones dentros de otra para ahorrar código, por ejemplo.
def esinpar(numero):
    if not espar(numero): #usamos el not para negar el valor booleano de espar
        return "si"
    else:
        return "no"
print('', esinpar(5), esinpar(4), '\n', espar(5), espar(4))
#Aumentemos un poco la complejidad de esta idea, para elevar la imaginación.
import math  # Importamos el módulo math para utilizar la constante pi (después analizamos más esto de los import)
# Función para calcular el área de un círculo
def area_circulo(radio):
    return math.pi * radio ** 2
# Función para calcular el volumen de un cilindro utilizando la función area_circulo()
def volumen_cilindro(radio, altura):
    area_base = area_circulo(radio)  # Calculamos el área de la base utilizando la función area_circulo()
    return area_base * altura
radio = 32
altura = 50
print("El área del círculo es:", area_circulo(radio))
print("El volumen del cilindro es:", volumen_cilindro(radio, altura))
#una función, como ya habrás notado, puede tener todos los parámetros que se necesiten, pudiendo ser mucho más de uno.
def resultado(valor1,valor2): #Si queremos más de 2 no podemos, solo 2
    return valor1*valor2 #ejemplo simple, siempre dvolverá el resultado de esto.
print(resultado(2,2))
#Si queremos que lo anterior se comporte como por ejemplo el sum() podemos hacer uso de for
def resultado2(valores):
    resultado = 1
    for valor in valores:
        resultado *= valor
    return resultado
print(resultado2(lis), resultado2([1,2,3,4]), resultado2([1,2,3,4,5,6]))
#librerías, estas son las que ingresamos con import como vimmos antes, hacen de todo, un ejemplo.
#NOTA: Todas las import deberían hacerse al inicio del código, aunque python no lo exije como otros lenguajes, es una buena práctica que aquí ignoraremos por razones de aprendizaje lineal.
import random as rd #genera núeros aleatorios, con el as asignamos un alias para evitar escribir random.algo()
print(rd.random(), rd.random()) #números aleatorios entre 0.0 y 1.0
print(rd.randint(1,500)) #numero aleatorio entre a y b valores enteros.
print(rd.uniform(1.0,500.0)) #numero aleatorio entre a y b valores flotantes.
cosas = ["uno","dos","tres","cuatro","cinco"]
print(rd.choice(lis), rd.choice(cosas)) #algo aleatorio de una secuencia dada, entero o caracter.
#Estos son los más fáciles, pero hay más ejemmplos que puedes invesgigar con tu IDE favorito.
#veamos otra
import datetime as fecha #usamos alias fecha
print(fecha.date.today()) #muestra la fecha en formato YYYY-MM-DD, la clase es date, el método today
#si queremos formatear la fecha usamos el método strftime()
fformat = fecha.date.today() #no se puede hacer esto fecha.date.today.strftime() asi que almacenamos en una variable.
print(fformat.strftime("%d-%m-%y"))
print(fecha.date.today().strftime("%d-%m-%y")) #aunque también se puede hacer esto, se convierte en tecto y luego ese texto se formatea.
print(fecha.date.today().strftime("%d-%m-%Y")) #la minúscula o mayúscula diferencia si se ve AAAA o AA

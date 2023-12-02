# Variables
number = 5
string = "String value"
email = "holamundo@gmail.com"
mi_var = "nombre de usario"
# _mi_var = "sfc"
miVarP = "fg1"
MIVAR23 = 23

a, b, c = "1", "5", "9"

valor1 = valor2 = valor3 = "Multiple variables"

inicio = "hola "
final = "mundo"

print(inicio + final)

palabra = "palabra es un string"
numero_entero = 4
numero_tipo_flow = 20.2
numero_complejo = 1j


# Lista es una collection de datos
lista = [1, 2, 3]
lista.append(4)

lista.clear()

lista2 = lista.copy()

lista2.count()
#index
lista[0]

# elimina ultimo elemeno de la lista
lista.pop()

# elimina un  elemeno especifico de la lista
lista.remove(1)

#dar vuelta una lista
lista.reverse()

#ordenar una lista
lista.sort() ## no se puede ordenar listas cuando contienen tipos de datos diferentes usando el metodo sort

print(lista)


# Duplas: se se pueden modificar, solo se pueden hacer nuevas duplas.
tupla = ("gol", "futbol") #tienen menos metodos que las listas
print(tupla)

#Metodos
tupla.index("gol")
print(tupla[0])

#Si queremos modificar una dupla, debemos convertirla en una lista:
listaDeDupla = list(tupla)
listaDeDupla.append("cancha")

# Tipo de datos: Rangos
rango = range(6)
print(rango)

# Diccionarios: se acceden a ellos mediante strings y no numeros como en las listas.
diccionario = {
 "nombre": "katie",
 "raza": "persa",
 "edad": "2"
}

print(diccionario)

## Acceder a los valores del diccionario:
print(diccionario["nombre"])
print(diccionario["raza"])

print(diccionario.get("nombre"))

#cambiar el valor de uno de los valores del diccionario
diccionario["nombre"] = "lofi"
print("diccionario")

# Contar cantidad de elenentos que contiene
print(len(diccionario))

diccionario["ronronea"] = "si"
print(diccionario)

#eliminar propiedad de diccionario
diccionario.pop("ronronea")
print(diccionario)

#Elimina el ultimo elelento
diccionario.popitem("ronronea")
del diccionario["ronronea"]

# copiar diccionario
diccionario.copy()
copia = dict(diccionario)

#Eliminar todos los elmentos del diccionario
diccionario.clear()

#Dictionarios anidados

fuffly = {
    "nombre": "Fluffy",
    "edad": 4
 }

mamba = {
    "nombre": "Mamba",
    "edad": 12
 },

katie = {
    "nombre": "Katie",
    "edad": 4
 }
gatitos = {
 "fluffly" : fuffly,
 "Mamba": mamba,
 "katie" : katie
}

print(gatitos)

#Creat diccionario con constructor dict
perritos = dict(nombre = "Katie", raza = "persa", edad = 4)
print(perritos)

#Booleanos
boleano = True
boleano2 = False


#Control de flujo
if 5 > 3: # Here is a comment in Python
 print("5 es mayor a 3")

a = True
b = True

if a == b:
 print("hola")

if 5 > 10:
 print("hola")

if a != b:
 print("Hola")

if 5 >= 10:
 print("hola")


###
if 5 >= 10:
 print("hola")
elif 11 > 10:
 print("hola")
else:
 print("Hola")

 ###
 if 5 >= 10:
  print("hola")
 else:
  print("Hola")

###### Oerador ternario
print("cuando devuelve true") if 11 > 10 else print("cuando devuelve false")

## And
if 11 > 10 and 14 > 10:
  print("Ambas devuelven true")

if 11 > 10 and 9 > 10:
  print("Hay una falsa, esto no se mostrara")

## Or
if 1 > 0 or 12 > 10:
  print("Una de las condiciones devolvio true")

if 1 > 2 or 9 > 10:
 print("si ambas condiciones evaluan false no se ejecuta el codigo")




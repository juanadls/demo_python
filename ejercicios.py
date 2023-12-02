dato = input("Ingrese dato: ")
print(dato)

lista = ["hola", "adios", "gol","feliz", "dragones"]

if lista.count(dato)  > 0 :
    print("El dato existe: ", dato)
else: 
    print("El dato no existe", dato)


#############################################
primero = input("Ingrese primer numero: ")
segundo = input("Ingrese segundo numero: ")

primerNumero = int(primero)
segundoNumero = int(segundo)

print(primerNumero, segundoNumero)

primero = input("Ingrese el primer numero: ")

try:
    primero= int(primero)
except: 
    primero = "No se pudo cambiar el tipo de input"

segundo = input("Ingrese el segundo numero: ")

try:
    segundo= int(segundo)
except: 
    segundo = "No se pudo cambiar el tipo de input"


if primero == "No se pudo cambiar el tipo de input" or segundo == "No se pudo cambiar el tipo de input":
  print("Ingresaste un mal dato. solo prueba con numeros")
else:
    print(primero + segundo)

    



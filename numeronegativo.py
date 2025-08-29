#Nombre: Programa para determinar si un numero es negativo o no
#Entradas: 
#El numero ingresado por el usuario
#Proceso de Salida: 
#Dependiendo del numero ingresado determina si es negativo o no usando la funcion if y else
#Salida:
#El resultado determina el mensaje que se le muestra en pantalla al usuario que puede ser "El numero es negativo" o "El numero no es negativo" 

numero = float(input("ingrese un numero "))
if numero < 0:
    print ("el numero es negativo")
else:
    print ("El numero no es negativo")
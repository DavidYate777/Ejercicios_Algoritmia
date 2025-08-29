#Nombre: Programa para determinar si un numero esta entre el rango de 100 y -100
#Entradas: 
#El numero ingresado por el usuario para determinar el rango
#Proceso de Salida: 
#Dependiendo del numero ingresado por el usuario se determina si esta dentro del rango
#Salida:
#El mensaje final que recibe el usuario, que puede ser tanto "El numero esta fuera del rango (100, -100)" 

#Le pide al usuario ingresar el numero
numero = float(input("Ingrese el numero"))
#Mediante el numero ingresado determinando si esta dentro del rango de 100 y -100 mediante la funcion if y else
#Dependiendo del resultado el mensaje que se le mostrara al usuario ser "El numero esta fuera del rango (100, -100) o si esta dentro del rango (100, -100)
if numero > 100 or numero < -100:
    print ("El numero esta fuera del rango (100, -100)")
else:
    print ("El numero esta dentro del rango")
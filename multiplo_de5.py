#Nombre: Programa para determinar si un numero es multiplo de 5
#Entradas: 
#El numero ingresado por el usuario
#Proceso de Salida: 
#Dependiendo del numero ingresado se determina si el numero es multiplo o no mediante la funcion if y else
#Salida:
#Segun el resultado obtenido se le muestra el mensaje en pantalla al usuario que puede ser "El numero es multiplo de 5" o "El numero no es multiplo de 5"


#Le pide al usuario ingresar el numero
numero = float(input("Ingrese el numero:"))

#Realiza una condicion la cual determina si el numero es multiplo de 5 o no
#Dependiendo del resultado se muestra un mensaje que puede ser "El numero es multiplo de 5" o "El numero no es multiplo de 5"
if numero % 5 == 0:
    print (f"El {numero} es multiplo de 5")
else:
    print (f"El {numero} no es multiplo")
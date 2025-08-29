#Nombre: Programa para determinar si el usuario nacio en un año bisiesto
#Entradas: 
#El año ingresado por el usuario
#Proceso de Salida: 
#Dependiendo del año ingresado por el usuario se determina si es bisiesto o no
#Salida:
#El mensaje final que recibe el usuario, que puede sar tanto "el año es bisiesto" o "El año no es biciesto"

#Se le pide a el usuario que ingrese el año
año = float(input("Ingrese el año"))

#Se realiza el proceso para determinar si el año ingresado por el usuario es bisiesto o no mediante la funcion if y else
#Dependiendo del resultado el usuario recibe el mensaje en pantalla que puede ser "El año es biciesto" o el "El año no es bisiesto"
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print (f"El {año} es bisiesto")
else:
    print (f"El {año} no es bisiesto")
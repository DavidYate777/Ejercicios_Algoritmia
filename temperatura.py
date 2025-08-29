#Nombre: Programa para determinar si la temperatura el correcta para congelar o no
#Entradas: 
#La temperatura ingresada por el usuario
#Proceso de Salida: 
#Dependiendo de la temperatura ingresada por el usuario determina si es apta o no para congelar mediante la funcion if y else
#Salida:
#El mensaje final que recibe el usuario, que puede ser "Esta apto para congelar" o "No es apto para congelar"

#Le pide al usuario ingresar la temperatura
temperatura = float (input ("Ingrese la temperatura "))
#Determina si la temperatura es apara para congelar mediante la funcion if o else
#Dependiendo del resultad se muestra le muestra en pantalla al usuario "Es apto para congelar" o "No es apto para congelar"
if temperatura <= 0:
    print ("Esta apto para congelar")
else:
    print ("No esta apto para congelar")
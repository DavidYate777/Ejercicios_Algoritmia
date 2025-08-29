#Nombre: Programa para determinar si una persona puede votar dentro del pais Colombia
#Entradas: 
#La edad ingresada por el usuaurio
#La nacionalidad ingresada por el usuario
#Proceso de Salida: 
#Determina si el usuario cumple con los parametros para votar segun lo ingresado 
#Salida:
#El mensaje final que recibe el usuario diciendole si es apto para votar o no

#Le pide al usuario sus datos de edad y nacionalidad
Edad = float(input("Ingrese su edad"))
Nacionalidad = input("Ingrese su nacionalidad")

#Determina si el usuario cumple con los parametros establecidos para votar
#El resultado determina el mensaje en pantalla que se le mostrar al usuario tanto como "Usted puede votar" o "Usted no puede votar"
if Edad >= 18 and Nacionalidad == "Colombia":
    print("Usted puede votar")
else:
    print("Usted no puede votar")
#Nombre: Programa para determinar si un estudiante aprobo o no
#Entradas: 
#La nota del estudiante ingresada por el usuario
#Proceso de Salida: 
#Dependiendo de la nota ingresada el if y el else determinan el mensaje para el usuario
#Salida:
#El mensaje final que recibe el usuario, que puede sar tanto "Aprobo" como "No Aprobo"

#Pide la nota al usuario
nota = float(input(f"Ingrese su nota"))
#Realiza una condicion
#Dependiendo de la nota ingresada el usuario recibe el mensaje
if nota < 60:
    print ("No Aprobo")
else:
    print ("Aprobo")
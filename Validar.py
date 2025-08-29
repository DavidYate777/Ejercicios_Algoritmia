#Nombre: Programa para validar si el usuario es administrador
#Entradas: 
#La contraseña ingresada por el usuario
#Proceso de Salida: 
#Mediante la función if y else determina si la contraseña ingresada es igual a "Admin"
#Salida:
#El mensaje final que recibe el usuario, que puede ser 
#"Usted es Administrador" o "Usted no es administrador"

#Le pide al usuario ingresar la contraseña
contraseña = input("Ingrese su contraseña: ")

#Verifica si la contraseña es "Admin" con if y else
if contraseña == ("Admin"):
    print("Usted es Administrador")
else:
    print("Usted no es administrador")

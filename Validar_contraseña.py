
#Nombre: Programa para validar la contraseña de administrador
#Entradas: 
#La contraseña ingresada por el usuario
#Proceso de Salida: 
#Mediante la función if y else determina si la contraseña coincide con la establecida (12344)
#Salida:
#El mensaje final que recibe el usuario, que puede ser 
#"Usted tiene permisos de administrador" o "Usted no tiene permisos"

#Le pide al usuario ingresar la contraseña
contraseña = float(input("Ingrese su contraseña: "))

#Verifica si la contraseña es correcta o no con if y else
if contraseña == 12344:
    print("Usted tiene permisos de administrador")
else:
    print("Usted no tiene permisos")

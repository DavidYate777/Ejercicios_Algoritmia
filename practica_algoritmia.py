#Nombre: Programa para obtener iniciales en mayuscula
#Entradas:
#     Variable y funcion
#     Variable y funcion
#Salidas:
#     Iniciales: Las primeras letras de nombre y apellido
#Proceso:
#     Pide el nombre de la persona y extrae la primera letra del nombre y apellido

#Pedir nombre y apellido
nombre = input("Ingresa tu nombre:")
apellido = input ("Ingrese su apellido:")

#Tomar la primera de cada uno y ponerla en mayuscula
iniciales = nombre [0].upper () + apellido [0].upper()

#Mostrar el resultado
print ("Tus iniciales son", iniciales)
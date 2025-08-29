#Nombre: Programa para determinar el tipo de triángulo según sus lados
#Entradas: 
#Los tres lados del triángulo ingresados por el usuario
#Proceso de Salida: 
#Dependiendo de la igualdad entre los lados, mediante la función if, elif y else determina si el triángulo es equilátero, isósceles o escaleno
#Salida:
#El mensaje final que recibe el usuario, que puede ser "El triángulo es equilátero", 
#"El triángulo es isósceles" o "El triángulo es escaleno"

#Le pide al usuario ingresar los tres lados
lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))
lado3 = float(input("Ingrese lado 3: "))

#Compara los lados mediante if, elif y else para determinar el tipo de triángulo
if lado1 == lado2 == lado3:
    print("El triángulo es equilátero")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("El triángulo es isósceles")
else:
    print("El triángulo es escaleno")


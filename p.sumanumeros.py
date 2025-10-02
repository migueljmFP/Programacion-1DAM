contador = 0
numero = int(input("Introduce un número:"))

while numero > -1:
	contador += numero
	numero = int(input("Introduce otro número:"))

print("La suma total de los números es:", contador)

#Ingresar 3 numeros y mostrar el mayor de los 3.

numero_mayor = 0
n1 =int(input("Ingrese un numero: "))
n2 =int(input("Ingrese un segundo numero: "))
n3 =int(input("Ingrese un tercer numero: "))

if n1 > n2:
    numero_mayor = n1
else:
    numero_mayor = n2

if numero_mayor > n3:
    print("El numero mayor es: ", numero_mayor)
else:
    print("El numero mayor es: ", n3)

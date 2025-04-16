n1 =int(input("Ingrese un numero."))
n2 =int(input("Ingrese un segundo numero."))
n3 =int(input("Ingrese un tercer numero"))

suma =(n1+n2+n3)

prom =(suma/3)

print("El promedio es: ", prom)



if prom >= 4.0:
    print("El alumno aprobó")
else:
    print("El alumno reprobo")
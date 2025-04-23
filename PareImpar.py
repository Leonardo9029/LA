cant = int (input("Ingrese la cantidad de numeros: "))

cant_pares=0
cant_impares=0



for i in range (cant):
    num=int (input("Ingrese un numero: "))
    if num %2==0:
        print("El numero es par ")
        cant_pares+=1
    else:
        print("El numero es impar ")
        cant_impares+=1

print(f"La cantidad de pares es: {cant_pares} y la cantidad de imares es: {cant_impares}")
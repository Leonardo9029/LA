# # deinir 2 candidatos. Definir cantidad de votatntes.
# preguntar a cada votante por quien votara mostrandolas alternativas. 
# Contar los votos y mostro resultados.
# definir el ganador y mostrar porcentaje de votos obtenidos.


#Definir candidatos:
c1 = "Profesor Rosa"
c2 = "SonGokú"

#/////////////////////
#Cantidad de votos de cada uno:
cv1 = 0 
cv2 = 0


print(f"Bienvenido a las elecciones presidenciales, los candidatos son: {c1} y {c2}")
print(f"Para votar por {c1}  eliga la opción 1 y para votar por {c2} eliga la opción 2")
print("////////////////////////////////////////////////////////////////////////////////")
cantvot = int(input("Defina la cantidad de votantes: "))

#//////////////////////////////////////////////////////////////////////}
#Ahora el for para las elecciones.

for i in range(cantvot):
    print(f"por quien votara? 1.-{c1} o 2.-{c2} ")
    voto =int(input("Escriba 1 o 2."))
    if voto == 1:
        cv1= cv1+1
    else:
        cv2=cv2+1


print(f"La cantidad de votos de {c1} fue: {cv1}")
print(f"La cantidad de votos de {c2} fue: {cv2}")


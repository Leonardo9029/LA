frase = input("Ingrese una frase")
c=0
v=0
for i in frase:
     #print(i)
    if i in "aeiou":
     v=v+1
    c+=1
print(f"La cantidad de vocales es: {v}")
print(f"La cantidad de caracteres es: {c}")
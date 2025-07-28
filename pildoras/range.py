#range es  un tipo de array

for i in range(5):
    print(f"el valor de la variable es:{i}") #indica q es una fnc del tipo f
    #sirve para concatenar distintos tipos de variables

for i in range(0,11): print(f" el numero {i} es entero")
for i in range(0,11, 2): print(f" el numero {i} es par")
for i in range(1,11, 2): print(f" el numero {i} es impar")

#len devuelve el numero de caracteres de un string
valido=False
email=input("ingresa tu email: ")

for i in range(len(email)):
    if email[i] =="@":
        valido=True

if valido: print("es correcto")
else: print("incorrecto")


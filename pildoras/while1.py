#while condicion:  (hasta que sea False)
i=1
while i<=10: 
    print("linea " + str(i))
    i=i +1
print("termino el run")

edad=int(input("ingresa edad: "))
while edad<5 or edad>100: #OR no AND
    print("edad negativa")
    edad=int(input("ingresa edad: "))

print("fin")
print("la edad es " + str(edad))

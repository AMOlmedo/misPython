print("programa de becas")
distancia=int(input("ingrese distacia: "))
print(distancia)              
bro=int(input("ingrese hermanos: "))
print(bro)
salario=int(input("ingrese salario: "))
print(salario)
#  operador logico AND ( y si ademas)
#  operador logico OR  (o si no)

if distancia >40 and bro >2 or salario<=2000:
    #se tienen que cumplir todas las condiciones
    print("tienes beca")
else: print("no tienes beca")


#  operador logico IN
# lower : todo a minuscula
# upper : todo a mayuscula

print("integrantes de la familia: ")
var1=input("ingresa el nombre")
nombre=var1.lower()

if nombre in("adrian", "marcela", "martina"):
    print( nombre+  " pertenece a la familia")
else:
    print("no es familia")





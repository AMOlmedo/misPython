##edad=int(input("ingrese la edad: "))
##if 0<edad<100: print("la edad es correcta")
##else: print("la edad  es incorrecta")

sueldo_pte= int(input("ingrese el sueldo presidente: "))
print("el salario del presidente es " + str(sueldo_pte))

sueldo_dir= int(input("ingrese el sueldo director: "))
print("el salario del presidente es " + str(sueldo_dir))

sueldo_jefe= int(input("ingrese el sueldo jefe: "))
print("el salario del presidente es " + str(sueldo_jefe))

sueldo_adm= int(input("ingrese el sueldo admin: "))
print("el salario del presidente es " + str(sueldo_adm))

if sueldo_adm < sueldo_jefe < sueldo_dir < sueldo_pte: #concatenacion de  operadores de comparacion
    
    print("todo esta ok")
else:
    print("los sueldos estan mal") 

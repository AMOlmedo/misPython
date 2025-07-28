# bucles determinados e indeterminados  (no sabemos cuantas veces)
#for  i  in [1,2,3]: # por cada elemento independiente del tipo o dato de la lista 
    #print(i, end=" ") #agrega un espacio despues de cada elm y en una linea
email=False
punto=False
addMail=input("ingrese la direccion de email: ")   
i=addMail
for i in addMail: 
    if (i== "@" ):
        email=True
    if (i== "."):
        punto=True  

if (email==True and punto==True): #por defecto la variables son True
    print("la direcccion de  email es correcto")
else:
    print(" la direccion de email es incorrecto")
#no funciona  con el punto, revisar







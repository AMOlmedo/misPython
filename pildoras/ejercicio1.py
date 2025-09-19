
num1=int(input("ingrese en primer numero: "))
num2=int(input("ingrese en segundo numero: "))

def DevuelveMax():
  
    if num1>num2:
        print("el num1 es mayor " + str(num1))
    else: 
        print("el num2 " + str(num2)+ " es mayor!" )

print(DevuelveMax())




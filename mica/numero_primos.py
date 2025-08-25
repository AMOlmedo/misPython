#ingresa un numero N y cuenta cuantos primos hay

def primos():
    cantidad= int(input("CANTIDAD DE NUMEROS PRIMOS: "))

    contador=0
    numero=2
    while contador < cantidad:
       if es_primo(numero):
           primos(numero, end= ' ')
           contador +=1
    numero +=1
    
def es_primo(num):
    if num <2:
        return False
    for i in range(int(2,num **0.5)+1):
        if num % i ==0:
            return False
    return True

print(primos())



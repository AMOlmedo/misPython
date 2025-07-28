## Generador

def generaPares(limite):
    num=1
   
    while num<limite:
        yield num*2
        num=num+1
    
devulvePares=generaPares(10)
for i in devulvePares:
    print(i)






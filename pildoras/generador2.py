def devuelve_cuidades(*ciudades):#NOTA: el asterisco * es para indicar 
# que no se conoce el valor del argumento, de decir, es indetermminado.
    for elemento in ciudades:
        yield elemento
#objeto generador 
ciudades_devueltas=devuelve_cuidades ("maipu", "lh", "lujan", "ciudad")

print(next(ciudades_devueltas)) #next devuelve el primer elemento
print(next(ciudades_devueltas)) # luego next el siguiente

    

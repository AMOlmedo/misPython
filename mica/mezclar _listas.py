#Mexclar los elementos de dos listas

import random

lista1=[1,2,3]
lista2=['a','b','c']

mezclada= lista1 + lista2
print(mezclada)    #original

random.shuffle(mezclada)
#shuffle "baraja los elementos"
print(mezclada)     #mezclada
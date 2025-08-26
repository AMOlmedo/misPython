#Calendario q muestra la fecha de hoy

import calendar #calendar es una libreria y datetime es otra
from datetime import datetime 

def calendario():
    hoy = datetime.now() #datetime.now() obtiene la fecha y hora actual
    day = hoy.day
    month = hoy.month
    year = hoy.year
    calendario = calendar.month(year, month) #calendar.month(año, mes) muestra el calendario del mes y año especificado
    day_color=calendario.replace(f"{day:2}",f"\033[91m{day:2}\033[0m") 
    #para pintar el dia de otro color se utiliza un ansi ??
    print(day_color)

calendario()

#El "código ANSI" para cambiar el color de un string en realidad son las secuencias de 
# escape ANSI, que son cadenas especiales de caracteres que la terminal interpreta para
# controlar el formato del texto, incluido el color, el estilo y el movimiento del cursor.
# Para cambiar el color, se antepone una secuencia como \u001B[XXm (donde XX es el código del color)
# a la cadena de texto y se utiliza el código de reinicio \u001B[0m al final para volver al 
# color predeterminado. 
#Ejemplos de códigos 
#\u001B[31m : Rojo
#\u001B[32m : Verde
#\u001B[34m : Azul
#\u001B[44m : Fondo azul
#\u001B[1;31m : Texto rojo claro (o brillante)
#
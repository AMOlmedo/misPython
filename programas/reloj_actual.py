# reloj que imprime la hora actual

print ("hora actual:")

import time
def reloj():
    while True:
        hora_actual=time.strftime("%H:%M:%S")
        print(hora_actual,end="\r")        
    time.sleep(1)
reloj()

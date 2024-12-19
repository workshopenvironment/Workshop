import math, random
from random import randint
from time import localtime, sleep
import time


def wuerfeln():
    return random.randint(1,6)

def aktueller_timestamp():
    z = localtime()
    a = print(z.tm_hour, 'Uhr', z.tm_min, 'min', z.tm_sec, 'Sec')
    return a
    #return int(time.time())
#timestamp = aktueller_timestamp()
#print(f"{timestamp}")

for i in range(5):
    print(wuerfeln(), end = ' ')
    sleep(2)
    aktueller_timestamp()    

# 2te Variante
for i in range(5):
    print("Wurf:", wuerfeln(), "Timestamp:", aktueller_timestamp(), end = '  ')
    sleep(2)    

f = open('text.txt', 'w')
f.write('Annelies Geburtstag: 15. November')
f.close()

g = open('text.txt', 'r')
erinnerung = g.read()
g.close()
print(erinnerung)

b = b'fdfwjjs-'
a = b.decode()
print(list(b))
print(a)

try:
    stream = open('text.txt', 'r')
    daten = stream.read()
    stream.close()
except:
    print("Fehler")    

stream = open('text.txt', 'w')
try:
    neu_datei = stream.write('Meine Daten')
except:
    print('Fehler!')
finally:
    stream.close()     
print(stream)
print(neu_datei, '+')

# Die ist gleich als den try: except: finally: aber kürzer und eleganter
with open('text.txt' , 'w') as stream:
    stream.write('Meine neuen Daten')

import pickle
liste = [1, 2, 3]
with open('liste.dat', 'wb') as stream:
    pickle.dump(liste, stream)
with open('liste.dat', 'rb') as stream:
    liste = pickle.load(stream)
print(liste)        
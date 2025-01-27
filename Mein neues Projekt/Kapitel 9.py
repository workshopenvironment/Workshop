for buchstabe in 'Abend':
    print(ord(buchstabe),  end = '   ')

print()
print(chr(98))
print(chr(100))
print(chr(65))
print(chr(0x10ffff))
print(chr(0x1F47D))
print(chr(0x2764))

print(chr(98),    chr(100),    chr(65), end = '  ')
print()
print("Pferd heißt auf Chinesisch \u99ac.")
print("\"ich bin tot\"")
#print("\N{Name}")

x = 'banana'

for idx in range (0,5):
    print (x[idx], "=", id(x[idx]))

s = "Die Subtraktion ist ein Ergebnis zwischen zwei Zahlen: heißt eine zahl ist subtrahiert mit einer anderen.".lower()
a = s.count('sub')
b = s.endswith('.')
c = s.split() # Mit split() wird eine Liste von Wörtern gebildet
d = s.strip()
e = set(c) # Mit set() wird aus der Liste eine Menge gebildet
f = set(d)
print(a, '\n', b, '\n', c, '\n', d)
print(e, '\n', f)

wetter = 'Regenschauer'
neues_wetter = wetter.replace('Regen', 'Hagel')
print(wetter + ', ' + neues_wetter)
print(f"\"{wetter}\" , \"{neues_wetter}\"")

print('   Guten  \n  Morgen  \n'.strip()) # Frage dazu: warum kann strip nicht \n zwischen Guten und Morgen entfernen?
print('   Guten \n Morgen \n'.strip())

print('-'.join(['1', '2', '3']))

y = {ord('ü'): 'ue'}
nachricht = 'üben'
print(nachricht.translate(y))

text = '{gewinner} hat {preis} Euro gewonnen. Herzlichen Glückwunsch, {gewinner}!'
text_1 = text.format(gewinner='Tom', preis=1000)
print(text_1)
text_2 = '{:3} {:6}'
for n in range(5):
    print(text_2.format(n, n**3))    
text_3 = 'Ergebnis: {:10.2f}'
print(text_3.format(12.3456))

import re
text_4 = '1001 Nacht. Ali Baba und die 40 Räuber.'
zahlen = re.findall('\d+', text_4)
print(zahlen)

text_5 = 'Ein Geist, huhuhuhu!'
gefunden = re.findall('huhu', text_5)
print(gefunden)

text_6 = 'Witten 58452 Berlin 10115' # Raw-String
reg= r'\d\d\d\d\d'
#reg = r'\d
gefunden = re.findall(reg, text_6)
print(gefunden)

from random import choice
PERSONEN = ['Tina', 'Anna', 'Kim', 'Niels']
gewinner = choice(PERSONEN)
print('Der Gewinner ist ' + gewinner + '.')

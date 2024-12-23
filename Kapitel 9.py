for buchstabe in 'Abend':
    print(ord(buchstabe),  end = '   ')
print(chr(98))

print("Pferd heißt auf Chinesisch \u99ac.")

s = "Die Subtraktion ist ein Ergebnis zwischen zwei Zahlen: heißt eine zahl ist subtrahiert mit einer anderen.".lower()
a = s.count('sub')
b = s.endswith('.')
c = s.split()
d = s.strip()
e = set(c)
f = set(d)
print(a, '\n', b, '\n', c, '\n', d)
print(e, '\n', f)

wetter = 'Regenschauer'
neues_wetter = wetter.replace('Regen', 'Hagel')
print(wetter + ', ' + neues_wetter)

print('   Guten \n Morgen \n'.strip()) # Frage dazu: warum kann strip nicht \n zwischen Guten und Morgen entfernen?

print('-'.join(['1', '2', '3']))

text = '{gewinner} hat {preis} Euro gewonnen. Herzlichen Glückwunsch, {gewinner}!'
text_1 = text.format(gewinner='Tom', preis=1000)
print(text_1)
text_2 = '{:3} {:6}'
for n in range(5):
    print(text_2.format(n, n**3))    
text_3 = 'Ergebnis: {:10.2f}'
print(text_3.format(12.3456))

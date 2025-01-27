print('Hallo Welt!')
ganz_zahl = 42
gleitkommazahl = 12.75
konvertierte_zahl = int(gleitkommazahl)
zahl = float(ganz_zahl)
print(f"Konvertierte Zahl: {konvertierte_zahl}")
print('Konvertierte Zahl: ', konvertierte_zahl)
print(f"Konvertierte Zahl 1: {zahl}")

a = len(str(100))
b = bool(str([]))
c = list(str(2*5))
print("Das Ergebnis von allen diese Werte lautet:", int(a), bool(b), str(c))
print("Das Ergebnis von allen diese Werte lautet:", a, b, c)
input('Programm beenden mit ENTER')

print('Berechnung des Bremswegs')
eingabe_geschwindigkeit = input('Geschwindigkeit in Meter pro Sekunde: ')
v = int(eingabe_geschwindigkeit)
eingabe_bremsverzögerung = input('Bremsverzögerung in Meter pro Sekundenquadrat: ')
a = int(eingabe_bremsverzögerung)
s = v**2 / (2*a)
print(s)

# fehler1.py
a = int(input('Zahl: '))
ergebnis = a**2
print(ergebnis)

list = [2, "kunde", 3.14, "3.14"]
print('Der Datentyp von der erste Element ist: ', type(list[0]))
print('Der Datentyp von der zweite Element ist: ', type(list[1]))
print('Der Datentyp von der dritte Element ist: ', type(list[2]))
print('Der Datentyp von der vierte Element ist: ', type(list[3]))

# Eingabe
str1 ="Die Antwort ist "
num = 37

# Verarbeitung
str2 = str(num)
print(str1 + str2)

print("Willkommen zum Fehlerfindungs-Quiz!")
zahl1 = int(input("Bitte gib eine Zahl ein: ")) 
zahl2 = int(input("Bitte gib eine andere Zahl ein: "))
ergebnis = zahl1 + zahl2
print("Das Ergebnis der Addition ist: ", ergebnis)

wort = "Bananenschale"
wort_1 = "Bananen Schale"
test = wort.count('a')
test_1 = wort_1.count('a')
print(test, test_1)

3 * 'Hoch' # HochHochHoch

wort = 'Raumschiff'
wort[0:4] # Raum

wort[2:4] # um

max(wort) # f Falsch !!! Warum ist die Antwort 'u' ???

zahlen = [1, 2] + [1, 2]
zahlen # [1 ,2, 1, 2]

zahlen.count(1) # nur 2 mal also 2

s = [(1, 2), (3, 4), (5, 6)]
s[0] # (1, 2)

s[0][1] # (1, 2, 3, 4) Falsch !!! Antwort ist 2

'Quadrat'[0] # 0 Falsch !!! Antwort ist 'Q'

s = [[]]
len(s) # 2 Falsch !!! Antwort ist 1

zahl = [n for n in range(0,101) if n % 4 == 0]
print(zahl)

s = ['Anne', 'Lion', 'Test', 'Paulin', 'Zebra']
anfang_buchstabe = [wort[0] for wort in s]
print(anfang_buchstabe)

s = ['Anne', 'Lion', 'anesthesia', 'Paulin', 'Anton', 'Esther', 'armure']
beginn_a_A = [wort for wort in s if wort[0] == 'a' or wort[0] == 'A']
beginn_A_a = [wort for wort in s if wort.lower().startswith('a')]
beginn = [wort for wort in s if wort[0] in 'aA']
print(beginn_a_A, '\n', beginn_A_a, '\n', beginn)

MENÜ = '''
(T)elefonnummer suchen 
(N)ame suchen 
(E)nde '''
liste = [('Matheo', '0201 461487'), ('Leo', '0178 9652789'), ('Marius','0177 3543488')]
print(MENÜ)    

BEISPIEL = ' Graph dargestellt '
G = {1: [2, 4], 2: [1, 3, 5], 3: [2, 5], 4: [1, 5], 5: [2, 3, 4, 6], 6: [5]} #1
def suche_weg(aktuell, ziel, besucht): #2
    besucht = besucht + [aktuell] #3
    if aktuell == ziel: #4
        return besucht
    else:
        for k in G[aktuell]: #5
            if k not in besucht: #6
                weg = suche_weg(k, ziel, besucht) #7
                if weg: #8
                    return weg
        return [] #9
while True: #10
    start = int(input("Start: "))
    ziel = int(input("Ziel: "))
    weg = suche_weg(start, ziel, [])
    print("Weg:", weg) #11
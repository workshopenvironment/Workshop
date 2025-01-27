#laufen = 'Nein' 
def enthalten(kollektion, zahl):
    for i in kollektion:
        if round(i) == round(zahl):
            return True
    return False
print(enthalten([1, 2, 3], 2.5))
print(enthalten([2, 5, 9], 9.78))

#laufen = input("Möchten Sie das Programm beenden? (Ja/Nein): ")    
print(round(number=1.23456, ndigits=5))
print(round(ndigits=2, number=1.23456))

def nachricht(text='', an=' Mensch'):
    return 'Hallo ' + an + '! ' + text
print(nachricht('Tina', 'Montag geht klar.'))
print(nachricht(an='Tina'))
print(nachricht('Kopf hoch!'))

print(1, 2, 3, sep="     ")

for i in range(10):
    print(i, end='  \n   ')

def f():
    global x
    x = 1
f()
print(x)

# def f(x):
#     print(x)
#     f(x/2)
# f(100)    

def fak(x):
    if x == 0:
        return 1
    else:
        ergebnis = (x) * fak(x-1)
        return ergebnis
zahl = input("Geben Sie eine natürliche Zahl ein: ")
while zahl:
   facultät = fak(int(zahl))
   print("Fakultät von", zahl, 'ist:', facultät)
   print()
   zahl = input("Geben Sie eine natürliche Zahl ein: ")

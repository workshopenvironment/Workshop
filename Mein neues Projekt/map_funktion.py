tiere = ['Affe', 'Rentier', 'Fuchs']
wortlängen = map(len, tiere)
liste_wortlängen = list(wortlängen)
print(liste_wortlängen)

def add(x,y):
    return x + y
summe = map(add, [1, 2, 3], [4, 5, 6])
print(summe)
print(list(summe))

summe = map(lambda x, y: x+y, [1,2,3], [4,5,6])
print(list(summe))

zahlen = filter(lambda x:x%4==0, range(20))
print(list(zahlen))

ergenbis = (lambda a,b: a**2 + b**2) (4, 5)
print(ergenbis)

ergebnis_1 = print(float(input('a: '))**2 + float(input('b: '))**2)
print(ergebnis_1)

# def volume(l, b, d=2):
#     v = l*b*d
#     return v
# while True:
#     l = float(input("Länge in cm: "))
#     b = float(input("Breite in cm: "))
#     d = input("Dicke in cm: ")
#     if d:
#         v = volume(l, b, float(d))
#     else:
#         v = volume(l, b)
#     print("Volume ist: ", v, 'cm^3')        

#TO DO
def ziffern(text):
    dezimalziffern = '0123456789' 
    s = len(list(map(lambda c: c if c in dezimalziffern else None, text)))
    return s
satz = print(input("Geben sien eine Satz ein! "))
print(ziffern(satz))
#     anzahl = 0
#     for buchstabe in ziffern(text):
#         if buchstabe in dezimalziffern:
#             anzahl += 1
#         return anzahl
# text_1 = print(input("Geben Sie einen Text ein: "))
# text_2 = ziffern(text_1)
# print(ziffern(text_2))    



def f(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 1 or n == 2:
        return 1
    memo[n] = f(n-1, memo) + f(n-2, memo)
    return memo[n]
zahl = input("Geben Sie ein zahl ein: ")
while zahl:
    fibo = f(int(zahl))
    print("Die Fibonacci zahl von: ", zahl, 'ist:', fibo )
    print()
    zahl = input("Geben Sie ein Zahl ein: ")
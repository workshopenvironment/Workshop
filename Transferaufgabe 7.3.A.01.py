import math, random
# n = 81
# a = random.randint(1, n)
# b = math.sqrt(n)
# print(a)
# print(b)

def erzeuge_zufallszahlen_liste(n):
    zufallszahlen_liste = [random.randint(1, 100) for _ in range(n)]
    return zufallszahlen_liste

def berechne_wurzeln(zufallszahlen_liste):
    wurzeln = [math.sqrt(zahl) for zahl in zufallszahlen_liste]
    return wurzeln
    
def sortiere_und_erzeuge_tupel(zufallszahlen_liste):
    sortierte_wurzeln = sorted(berechne_wurzeln(zufallszahlen_liste))
    return [(zufallszahlen_liste[i], sortierte_wurzeln[i]) for i in range(len(zufallszahlen_liste))]
    #tupel_liste = [(a, math.sqrt(a)) for a in liste]
    #return tupel_liste

def erstelle_dictionary(tupel_liste):
    return {tupel[0] : tupel[1] for tupel in tupel_liste}
    #dictionary = [{a : [math.sqrt(a)]} for a in tupel_liste]
    #return dictionary

def main():
    zufallszahlen_liste = erzeuge_zufallszahlen_liste(10)
    print(zufallszahlen_liste)
    sortierte_wurzeln = sorted(zufallszahlen_liste)
    print(sortierte_wurzeln)
    wurzeln_liste = berechne_wurzeln(sortierte_wurzeln)
    print(wurzeln_liste)
    tupel_liste = sortiere_und_erzeuge_tupel(sortierte_wurzeln)
    print(tupel_liste)
    dictionary = erstelle_dictionary(tupel_liste)
    print(dictionary)
    print(f"Der Wert von ‚dictionary‘ ist {dictionary} und sein Klassentyp ist {type(dictionary).__name__}.")

main()    

# MENÜ = '''
# 1- Zufälligen Zahlen erzeugen (Z)
# 2- Quadratwurzeln berechnen (Q)
# 3- Liste sortieren (L)
# 4- Tupel erstellen (T)
# 5- Dictionary erstellen und ausgeben (D)'''
# eingabe = input("Whälen Sie bitte eine Option: (Z, Q, L, T, D)")
# print(MENÜ)
# #while eingabe:
# if eingabe == 'Z':
#     #n = 10
#     z = erzeuge_zufallszahlen_liste(10)
#     print(z)
# elif eingabe == 'Q':
#     q = berechne_wurzeln(erzeuge_zufallszahlen_liste)
#     print(q)
# elif eingabe == 'L' or eingabe == 'T':
#     lt = sortiere_und_erzeuge_tupel(erzeuge_zufallszahlen_liste)
#     print(lt)
# elif eingabe == 'D':
#     d = erstelle_dictionary(sortiere_und_erzeuge_tupel)
#     print(d)
# else:
#     input("Ungültige eingabe. Geben Sie erneut eine Option: (Z, Q, L, T, D)")
# #print("Programm beendet.")    







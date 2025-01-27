print("Geben Sie bitte einen Name ein !")
name = input('Name: ')
gruß = 'Hallo ' + name + '!'
print(gruß)

print("Berechnung des Volumens eines Zylinders")
eingabe_höhe = input('Höhe in Meter: ')
eingabe_durchmesser = input('Durchmesser in Meter: ')
h = float(eingabe_höhe)
d = float(eingabe_durchmesser)
gleitkommazahl = 3.14
Volume = (d/2)**2 * gleitkommazahl * h
print("Das Volumen beträgt: ", str(Volume) + " Kubikmeter")
print('Das Volumen beträgt: ', Volume, ' Kubimeter.')
#input('Programm beenden mit ENTER')

a = 0
while a < 7:
    a = a + 1
    print(a, a**2, a**3)

def fallhöhe(t):
    g = 9.81
    s = 0.5*g * t**2
    return s
zeit = float(input('Fallzeit in Sekunden: '))
höhe = fallhöhe(zeit)
print('Die Fallhöhe diesen Brunnen beträgt: ', höhe, 'Meter.')
print('Die Fallhöhe diesen Brunnen beträgt: ', round(höhe,2), 'Meter.')

def fallhöhe_erde(t, g=9.81):
    e = 0.5*g * t**2
    return e
while True:
    t = float(input("Geben Sie fie Fallhöhe in Sekunden ein: "))
    g = input("Geben Sie die Gravitation/beschleunigung ein: ")
    if g:
        e = fallhöhe_erde(t, float(g))
    else:    
        e = fallhöhe_erde(t)
    print('Die Fallhöhe diesen Brunnen beträgt: ', e, 'm.')
    

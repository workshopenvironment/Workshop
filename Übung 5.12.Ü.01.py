def filtere_gerade_zahlen(zahl_listen):
    if not zahl_listen:
        return None
    gerade_zahl = list(filter(lambda x: x % 2 == 0, zahl_listen))
    return gerade_zahl
liste = [1,2,3,4,5,6,7,8,9,10]
gerade_zahl = filtere_gerade_zahlen(liste)
print(f"Die Liste von geraden Zahlen in dieser Liste ist: {gerade_zahl}")

def filtere_gerade_zahlen(liste_zahlen):
    #assert type(liste_zahlen) == list # liste_zahlen ist eine Liste
    assert isinstance(liste_zahlen, list) # Das Argument muss eine Öiste sein
    return [zahl for zahl in liste_zahlen if zahl % 2 == 0]

def sortiere_liste(zahlen):
    assert isinstance(zahlen, list)
    if len(zahlen) <= 1:
        return zahlen
    else:
        pivot = zahlen[0]
        zahlen_1 = [ x for x in zahlen[1:] if x < pivot]
        zahlen_2 = [ x for x in zahlen[1:] if x >= pivot]
        return sortiere_liste(zahlen_1) + [pivot] + sortiere_liste(zahlen_2)
    
def main():
    s = [-65, 1, 2, 5, 6, 9, 10, -20, 165, 124, -2, 15, 0, -789, 78]
    filter_liste = filtere_gerade_zahlen(s)
    sortierte_liste = sortiere_liste(filter_liste)
    print(f"Gefilterte und sortierte Liste sieht so aus: {sortierte_liste}")

if __name__ == "__main__":
    main()
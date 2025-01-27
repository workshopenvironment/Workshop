import os

def ist_sortiert(liste_zahlen):
    # i = 0
    # liste_zahlen[i] <= liste_zahlen[i+1] 
    # return [liste_zahlen for i in range(len(liste_zahlen)-1)]
    liste = all(liste_zahlen[i] <= liste_zahlen[i+1] for i in range(len(liste_zahlen)-1))
    print(liste)
    return liste

def verbessere_quicksort(liste_zahlen):
    assert not ist_sortiert(liste_zahlen), "Die Liste ist bereits sortiert."
    
    def quicksort(liste_zahlen):
        if len(liste_zahlen) <= 1:
            return liste_zahlen
        else:
            pivot = liste_zahlen[0]
            kleiner_al_pivot = [zahl for zahl in liste_zahlen[1:] if zahl < pivot]
            größer_als_pivot = [zahl for zahl in liste_zahlen[1:] if zahl >= pivot]
            return quicksort(kleiner_al_pivot) + [pivot] + quicksort(größer_als_pivot)

    debug = os.getenv('DEBUG', 'False') == 'True'
    if debug:
        print("Vor der Sortierung: ", liste_zahlen)
    sortiere_liste = quicksort(liste_zahlen)
    if debug:
        print("Nach der Sortierung: ", sortiere_liste)    

    return sortiere_liste    

def main():
    #s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    s = [-65, 1, 2, 5, 6, 9, 10, -20, 165, 124, -2, 15, 0, -789, 78]
    sortierte_liste = verbessere_quicksort(s)
    print(f"Sortierte Liste sieht so aus: {sortierte_liste}")

if __name__ == "__main__":
    main()    
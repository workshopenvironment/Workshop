print('Welche Stimmung besitzen Sie gerade?')
print("a) glücklich \nb) traurig\nc) müde")
#beenden = 'Nein'
antwort = input("Geben Sie Ihre Antwort(a, b, c): ") 
while True: #antwort not in ['a', 'b', 'c']:
    print("Geben Sie bitte eine gültige Antwort. Bitte wähle a, b oder c.")
    antwort = input("Geben Sie Ihre Antwort(a, b, c): ")
    if antwort == 'a':
        richtige_antwort = antwort
        print("Es ist toll zu hören, dass du glücklich bist!")
    elif antwort == 'b':
        richtige_antwort_1 = antwort
        print("Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!")           
    elif antwort == 'c':
        richtige_antwort_2 = antwort
        print("Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.")
    else:
        print("Sie haben keine gültige Antwort eingegeben")
        print("Interessant! Ich weiß nicht viel über diese Stimmung.")        
    beenden = input("Möchten sie das programm beenden? (Ja/Nein): ")
    if beenden.lower() == 'ja':
        break

# # Dieses Skript fragt den Benutzer nach seiner Stimmung und gibt basierend darauf eine Antwort aus.

# # Initialisiere eine Variable, um die Schleife zu steuern

# fortfahren = 'Nein'

# while fortfahren.lower() != 'ja':
#     # Schritt a: Eingabe der aktuellen Stimmung
#     stimmung = input("Wie ist deine aktuelle Stimmung? (glücklich, traurig, müde): ")

#     # Schritt b: Überprüfung der Eingabe und Ausgabe einer entsprechenden Nachricht

#     if stimmung == 'glücklich':
#         print("Es ist toll zu hören, dass du glücklich bist!")
#     elif stimmung == 'traurig':
#         print("Es tut mir leid zu hören, dass du traurig bist. Ich hoffe, es geht dir bald besser!")
#     elif stimmung == 'müde':
#         print("Vielleicht solltest du dich etwas ausruhen. Ruhe ist wichtig.")
#     else:
#         print("Interessant! Ich weiß nicht viel über diese Stimmung.")

#     # Schritt d: Abfrage, ob das Programm beendet werden soll

#     fortfahren = input("Möchtest du das Programm beenden? (Ja/Nein): ")  
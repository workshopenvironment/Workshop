zahl = int(input("Geben Sie eine Zahl ein! "))
isPrime = True
if zahl <= 1:
    isPrime = False
    print(f"Die Zahl: {zahl} ist keine Primzahl")
else:    
    for i in range(2, zahl):
        if zahl % i == 0:
            isPrime = False
            #print(f"Die Zahl: {zahl} ist keine Primzahl")
    if isPrime == True:
        print(f"Die Zahl: {zahl} ist eine Primzahl")
    else:
        print(f"Die Zahl: {zahl} ist keine Primzahl")

# zahl = int(input("Bitte Zahl eingeben: "))
# isPrime = True
# if zahl == 1:
#     print(f"Die Zahl: {zahl} ist keine Primzahl")
# else:
#     for number in range(2,zahl):
#         if zahl % number == 0:
#             isPrime = False
# if isPrime == True:
#     print("Primzahl")
# else:
#     print("Keine Primzahl")                

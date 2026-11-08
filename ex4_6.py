nombre = int(input("Entier positif : "))
while nombre < 0:
    print("  Il faut un entier positif.")
    nombre = int(input("Entier positif : "))

n = nombre
binaire = ""
if n == 0:
    binaire = "0"
while n > 0:
    binaire = str(n % 2) + binaire  
    n //= 2

print(f"Entier : {nombre} -> Binaire : {binaire}   (bin({nombre}) = {bin(nombre)})")
print("Verification :", "OK" if binaire == bin(nombre)[2:] else "ERREUR")

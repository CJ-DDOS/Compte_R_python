
n = int(input("Entier entre 1 et 10 : "))
while n < 1 or n > 10:
    print("  Valeur hors limites.")
    n = int(input("Entier entre 1 et 10 : "))

for i in range(1, 11):
    print(f"{n:2} x {i:2} = {n * i:3}")

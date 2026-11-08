n = int(input("Entier positif n : "))
while n < 0:
    print("  Il faut un entier positif.")
    n = int(input("Entier positif n : "))

somme = 0
factorielle = 1
for i in range(1, n + 1):
    somme += i
    factorielle *= i

print(f"Somme de 1 a {n} = {somme}")
print(f"{n}! = {factorielle}")

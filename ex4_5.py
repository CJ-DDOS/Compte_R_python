nombre = int(input("Entier : "))
while nombre <= 0:
    print("  Il faut un entier strictement positif.")
    nombre = int(input("Entier : "))

n = nombre
nb_chiffres = 0
somme = 0
inverse = 0
while n > 0:
    chiffre = n % 10          
    nb_chiffres += 1
    somme += chiffre
    inverse = inverse * 10 + chiffre
    n //= 10                  

print(f"Entier : {nombre} -> {nb_chiffres} chiffres ; somme = {somme} ; inverse = {inverse}")

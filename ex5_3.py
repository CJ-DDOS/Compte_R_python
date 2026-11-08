somme = 0
compteur = 0
while True:
    nombre = float(input("Nombre (0 pour terminer) : "))
    if nombre == 0:
        break                                   
    if nombre < 0:
        print("  Nombre negatif ignore.")
        continue                                
    somme += nombre
    compteur += 1
assert compteur > 0, "Aucune valeur positive n'a ete saisie"
moyenne = somme / compteur
print(f"Somme    : {somme:.2f}")
print(f"Valeurs  : {compteur}")
print(f"Moyenne  : {moyenne:.2f}")
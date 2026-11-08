
phrase = input("Phrase : ").lower()

frequences = {}
for caractere in phrase:
    if caractere.isalpha():                       
        frequences[caractere] = frequences.get(caractere, 0) + 1


for lettre in sorted(frequences):
    nb = frequences[lettre]
    print(f"{lettre} : {nb} " + "*" * nb)


lettre_max = ""
nb_max = 0
for lettre, nb in frequences.items():
    if nb > nb_max:
        lettre_max = lettre
        nb_max = nb
print(f"Lettre la plus frequente : {lettre_max} ({nb_max} fois)")

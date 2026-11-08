
inscrits = ["Amine", "Sarra", "Yassine", "Nour", "Omar"]

prenom = input("Prenom a rechercher : ").strip().lower()

for indice, inscrit in enumerate(inscrits):
    if inscrit.lower() == prenom:        
        print(f"{inscrit} est inscrit(e) a la position {indice + 1}.")
        break
else:
    print("Non inscrit")

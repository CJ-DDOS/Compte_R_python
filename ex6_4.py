etudiants = ["Ahmed", "Sarra", "Mohamed"]
matieres = ["Python", "Algo", "BD", "Reseaux"]
notes = [[12, 15, 9, 14],
         [18, 16, 17, 15],
         [8, 10, 11, 9]]

print(f"{'':10}", end="")
for matiere in matieres:
    print(f"{matiere:>9}", end="")
print(f"{'Moyenne':>10}")

sommes_colonnes = [0] * len(matieres)
moyennes_etudiants = []
for i, etudiant in enumerate(etudiants):
    print(f"{etudiant:10}", end="")
    somme_ligne = 0
    for j, note in enumerate(notes[i]):
        print(f"{note:9}", end="")
        somme_ligne += note
        sommes_colonnes[j] += note
    moyenne_ligne = somme_ligne / len(matieres)
    moyennes_etudiants.append(moyenne_ligne)
    print(f"{moyenne_ligne:10.2f}")

print(f"{'Moyenne':10}", end="")
for j in range(len(matieres)):
    print(f"{sommes_colonnes[j] / len(etudiants):9.2f}", end="")
print()

print()
for j, matiere in enumerate(matieres):
    meilleure_note = -1
    meilleur_etudiant = ""
    for i, etudiant in enumerate(etudiants):
        if notes[i][j] > meilleure_note:
            meilleure_note = notes[i][j]
            meilleur_etudiant = etudiant
    print(f"Meilleure note en {matiere:8}: {meilleure_note} ({meilleur_etudiant})")

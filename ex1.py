



SEUIL_ADMISSION = 10
SEUIL_RATTRAPAGE = 8
NOTE_ELIMINATOIRE = 6

nom = input("Nom de l'etudiant : ").strip().title()
cc = float(input("Note de CC (0-20) : "))
examen = float(input("Note d'examen (0-20) : "))
assiduite = input("Assiduite >= 80 % ? (o/n) : ").strip().lower()


if 0 <= cc <= 20 and 0 <= examen <= 20:  
    moyenne = cc * 0.4 + examen * 0.6

    
    if moyenne >= 16:
        mention = "Tres Bien"
    elif moyenne >= 14:  
        mention = "Bien"
    elif moyenne >= 12:  
        mention = "Assez Bien"
    elif moyenne >= SEUIL_ADMISSION:
        mention = "Passable"
    else:  
        mention = "Aucune"

    
    
    if moyenne >= SEUIL_ADMISSION and examen >= NOTE_ELIMINATOIRE:
        decision = "Admis"
    elif moyenne >= SEUIL_RATTRAPAGE:  
        if assiduite == "o":  
            decision = "Rattrapage"
        else:
            decision = "Ajourne (assiduite insuffisante)"
    else:
        decision = "Ajourne"  

    
    print("-" * 40)
    print(f"Etudiant : {nom}")
    print(f"Moyenne  : {moyenne:.2f}")  
    print(f"Mention  : {mention}")
    print(f"Decision : {decision}")
    print("-" * 40)
else:  
    print("Erreur : les notes doivent etre comprises entre 0 et 20.")

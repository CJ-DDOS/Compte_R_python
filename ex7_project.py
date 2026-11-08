COEF_CC = 0.4
COEF_EXAMEN = 0.6
SEUIL_ADMISSION = 10

classe = []
continuer = True

while continuer:
    print("\n=== GESTION DE LA CLASSE ===")
    print("1. Ajouter un étudiant")
    print("2. Afficher la classe")
    print("3. Rechercher par matricule")
    print("4. Rechercher par nom")
    print("5. Modifier les notes")
    print("6. Supprimer un étudiant")
    print("7. Statistiques")
    print("8. Classement")
    print("9. Quitter")

    choix_valide = False
    while not choix_valide:
        try:
            choix = int(input("Votre choix : "))
            if 1 <= choix <= 9:
                choix_valide = True
            else:
                print(f"Erreur : le choix {choix} n'est pas valide.")
        except ValueError:
            print("Erreur : entrez un nombre entier entre 1 et 9.")

    match choix:
        case 1:
            matricule_valide = False
            while not matricule_valide:
                try:
                    matricule = int(input("Matricule : "))
                    matricule_valide = True
                except ValueError:
                    print("Erreur : le matricule doit être un nombre entier.")

            matricule_unique = True
            for etudiant in classe:
                if etudiant["matricule"] == matricule:
                    print(f"Erreur : le matricule {matricule} existe déjà.")
                    matricule_unique = False
                    break

            if matricule_unique:
                nom = input("Nom : ").strip().title()
                prenom = input("Prénom : ").strip().title()

                notes_valides = False
                while not notes_valides:
                    try:
                        cc = float(input("Note de CC : "))
                        examen = float(input("Note d'examen : "))
                        if 0 <= cc <= 20 and 0 <= examen <= 20:
                            notes_valides = True
                        else:
                            print("Erreur : les notes doivent être comprises entre 0 et 20.")
                    except ValueError:
                        print("Erreur : entrez des notes numériques.")

                moyenne = COEF_CC * cc + COEF_EXAMEN * examen
                if moyenne >= 16:
                    mention = "Tres Bien"
                elif moyenne >= 14:
                    mention = "Bien"
                elif moyenne >= 12:
                    mention = "Assez Bien"
                elif moyenne >= SEUIL_ADMISSION:
                    mention = "Passable"
                else:
                    mention = "Ajourne"

                classe.append({
                    "matricule": matricule,
                    "nom": nom,
                    "prenom": prenom,
                    "cc": cc,
                    "examen": examen,
                    "moyenne": moyenne,
                    "mention": mention
                })
                print(f"L'étudiant {prenom} {nom} a été ajouté avec succès.")

        case 2:
            print("+------+--------------+-----------+-------+-------+---------+")
            print("| Mat. | Nom          | Prenom    | CC    | Exam  | Moyenne |")
            print("+------+--------------+-----------+-------+-------+---------+")
            for etudiant in classe:
                print(
                    f"| {etudiant['matricule']:4} | {etudiant['nom']:<12} | "
                    f"{etudiant['prenom']:<9} | {etudiant['cc']:5.2f} | "
                    f"{etudiant['examen']:5.2f} | {etudiant['moyenne']:7.2f} |"
                )
            print("+------+--------------+-----------+-------+-------+---------+")
            print(f"Nombre total : {len(classe)} étudiant(s)")

        case 3:
            matricule_valide = False
            while not matricule_valide:
                try:
                    matricule_recherche = int(input("Matricule à rechercher : "))
                    matricule_valide = True
                except ValueError:
                    print("Erreur : le matricule doit être un nombre entier.")

            etudiant_trouve = None
            for etudiant in classe:
                if etudiant["matricule"] == matricule_recherche:
                    etudiant_trouve = etudiant
                    break

            if etudiant_trouve is None:
                print(f"Etudiant introuvable pour le matricule {matricule_recherche}.")
            else:
                print(f"=== FICHE DE {etudiant_trouve['prenom']} {etudiant_trouve['nom']} ===")
                print(f"Matricule : {etudiant_trouve['matricule']:d}")
                print(f"Nom       : {etudiant_trouve['nom']}")
                print(f"Prenom    : {etudiant_trouve['prenom']}")
                print(f"CC        : {etudiant_trouve['cc']:.2f}")
                print(f"Examen    : {etudiant_trouve['examen']:.2f}")
                print(f"Moyenne   : {etudiant_trouve['moyenne']:.2f}")
                print(f"Mention   : {etudiant_trouve['mention']}")

        case 4:
            nom_recherche = input("Nom à rechercher : ").strip().casefold()
            resultats = []
            for etudiant in classe:
                if nom_recherche in etudiant["nom"].casefold():
                    resultats.append(etudiant)

            if resultats:
                for etudiant in resultats:
                    print(
                        f"{etudiant['prenom']} {etudiant['nom']} "
                        f"(matricule {etudiant['matricule']:d}) - "
                        f"Moyenne : {etudiant['moyenne']:.2f}"
                    )
            else:
                print(f"Aucun étudiant trouvé pour le nom « {nom_recherche} ».")

        case 5:
            matricule_valide = False
            while not matricule_valide:
                try:
                    matricule_recherche = int(
                        input("Matricule de l'étudiant à modifier : ")
                    )
                    matricule_valide = True
                except ValueError:
                    print("Erreur : le matricule doit être un nombre entier.")

            etudiant_trouve = None
            for etudiant in classe:
                if etudiant["matricule"] == matricule_recherche:
                    etudiant_trouve = etudiant
                    break

            if etudiant_trouve is None:
                print(f"Etudiant introuvable pour le matricule {matricule_recherche}.")
            else:
                notes_valides = False
                while not notes_valides:
                    try:
                        nouveau_cc = float(input("Nouvelle note de CC : "))
                        nouvel_examen = float(input("Nouvelle note d'examen : "))
                        if 0 <= nouveau_cc <= 20 and 0 <= nouvel_examen <= 20:
                            notes_valides = True
                        else:
                            print("Erreur : les notes doivent être comprises entre 0 et 20.")
                    except ValueError:
                        print("Erreur : entrez des notes numériques.")

                etudiant_trouve["cc"] = nouveau_cc
                etudiant_trouve["examen"] = nouvel_examen
                etudiant_trouve["moyenne"] = (
                    COEF_CC * nouveau_cc + COEF_EXAMEN * nouvel_examen
                )
                if etudiant_trouve["moyenne"] >= 16:
                    etudiant_trouve["mention"] = "Tres Bien"
                elif etudiant_trouve["moyenne"] >= 14:
                    etudiant_trouve["mention"] = "Bien"
                elif etudiant_trouve["moyenne"] >= 12:
                    etudiant_trouve["mention"] = "Assez Bien"
                elif etudiant_trouve["moyenne"] >= SEUIL_ADMISSION:
                    etudiant_trouve["mention"] = "Passable"
                else:
                    etudiant_trouve["mention"] = "Ajourne"
                print(
                    f"Notes modifiées. Nouvelle moyenne : "
                    f"{etudiant_trouve['moyenne']:.2f}"
                )

        case 6:
            matricule_valide = False
            while not matricule_valide:
                try:
                    matricule_recherche = int(
                        input("Matricule de l'étudiant à supprimer : ")
                    )
                    matricule_valide = True
                except ValueError:
                    print("Erreur : le matricule doit être un nombre entier.")

            indice_trouve = -1
            for indice, etudiant in enumerate(classe):
                if etudiant["matricule"] == matricule_recherche:
                    indice_trouve = indice
                    break

            if indice_trouve == -1:
                print(f"Etudiant introuvable pour le matricule {matricule_recherche}.")
            else:
                confirmation = input("Confirmer la suppression (o/n) : ").strip().casefold()
                if confirmation == "o":
                    etudiant_supprime = classe.pop(indice_trouve)
                    print(
                        f"L'étudiant {etudiant_supprime['prenom']} "
                        f"{etudiant_supprime['nom']} a été supprimé."
                    )
                elif confirmation == "n":
                    print("Suppression annulée.")
                else:
                    print("Confirmation invalide : suppression annulée.")

        case 7:
            if not classe:
                print("Aucun étudiant dans la classe : statistiques indisponibles.")
            else:
                nombre_etudiants = 0
                somme_moyennes = 0
                nombre_admis = 0
                mentions = {
                    "Tres Bien": 0,
                    "Bien": 0,
                    "Assez Bien": 0,
                    "Passable": 0,
                    "Ajourne": 0
                }
                meilleur = classe[0]
                plus_faible = classe[0]

                for etudiant in classe:
                    nombre_etudiants += 1
                    somme_moyennes += etudiant["moyenne"]
                    if etudiant["moyenne"] >= SEUIL_ADMISSION:
                        nombre_admis += 1
                    if etudiant["moyenne"] > meilleur["moyenne"]:
                        meilleur = etudiant
                    if etudiant["moyenne"] < plus_faible["moyenne"]:
                        plus_faible = etudiant
                    mentions[etudiant["mention"]] += 1

                nombre_ajournes = nombre_etudiants - nombre_admis
                moyenne_classe = somme_moyennes / nombre_etudiants
                pourcentage_admis = nombre_admis / nombre_etudiants * 100
                pourcentage_ajournes = nombre_ajournes / nombre_etudiants * 100

                print("=== STATISTIQUES DE LA CLASSE ===")
                print(f"Nombre d'étudiants : {nombre_etudiants:d}")
                print(f"Moyenne de la classe : {moyenne_classe:.2f}")
                print(
                    f"Meilleur(e) : {meilleur['prenom']} {meilleur['nom']} "
                    f"({meilleur['moyenne']:.2f})"
                )
                print(
                    f"Plus faible : {plus_faible['prenom']} {plus_faible['nom']} "
                    f"({plus_faible['moyenne']:.2f})"
                )
                print(
                    f"Nombre d'admis : {nombre_admis:d} / {nombre_etudiants:d} "
                    f"({pourcentage_admis:.2f}%)"
                )
                print(
                    f"Nombre d'ajournés : {nombre_ajournes:d} / {nombre_etudiants:d} "
                    f"({pourcentage_ajournes:.2f}%)"
                )
                print(f"Répartition : {mentions}")

        case 8:
            classement = sorted(
                classe,
                key=lambda etudiant: etudiant["moyenne"],
                reverse=True
            )
            print("=== CLASSEMENT ===")
            for rang, etudiant in enumerate(classement, start=1):
                print(
                    f"{rang:d}. {etudiant['prenom']} {etudiant['nom']} "
                    f"{etudiant['moyenne']:.2f} {etudiant['mention']}"
                )

        case 9:
            continuer = False
            print("Au revoir !")

        case _:
            print(f"Erreur : le choix {choix} n'est pas valide.")

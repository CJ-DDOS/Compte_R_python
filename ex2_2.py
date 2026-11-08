
mois = int(input("Mois : "))
annee = int(input("Annee : "))

match mois:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print(f"Le mois {mois} compte 31 jours.")
    case 4 | 6 | 9 | 11:
        print(f"Le mois {mois} compte 30 jours.")
    case 2:
        
        if (annee % 4 == 0 and annee % 100 != 0) or annee % 400 == 0:
            print(f"Fevrier {annee} compte 29 jours.")
        else:
            print(f"Fevrier {annee} compte 28 jours.")
    case _:
        print("Mois invalide.")

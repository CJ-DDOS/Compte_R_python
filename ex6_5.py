contacts = {"Amine": "20111222", "Sara": "22333444", "Yassine": "24555666"}
print("a) Liste des contacts")
for numero_ordre, (nom, tel) in enumerate(contacts.items(), start=1):
    tel_formate = tel[:2] + " " + tel[2:5] + " " + tel[5:]
    print(f"{numero_ordre}. {nom:8} {tel_formate}")
print("\nb) Numeros commencant par 2 + chiffre pair")
for nom, tel in contacts.items():
    if tel[0] == "2" and int(tel[1]) % 2 == 0:
        print(f"{nom} : {tel}")
inverse = {}
for nom, tel in contacts.items():
    inverse[tel] = nom
print("\nc) Recherche inverse")
numero = input("Numero a rechercher : ").strip().replace(" ", "")
if numero in inverse:
    print(f"Ce numero appartient a {inverse[numero]}.")
else:
    print("Numero inconnu.")
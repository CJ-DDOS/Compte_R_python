
age = int(input("Age : "))
etudiant = input("Etudiant (o/n) : ").strip().lower()
jour = input("Jour : ").strip().lower()


if age < 12:
    tarif = 5
elif etudiant == "o" and age < 26:
    tarif = 7
elif age >= 65:
    tarif = 6
else:
    tarif = 10

if jour == "mardi":
    tarif = tarif * 0.8  

print(f"Tarif a payer : {tarif:.2f} DT")

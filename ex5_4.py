
import random

MAX_TENTATIVES = 7
secret = random.randint(1, 100)

tentatives = 0
while tentatives < MAX_TENTATIVES:
    proposition = int(input(f"Proposition ({tentatives + 1}/{MAX_TENTATIVES}) : "))
    if proposition < 1 or proposition > 100:
        print("  Proposition refusee : entrez un nombre entre 1 et 100.")
        continue                                 
    tentatives += 1
    if proposition == secret:
        print(f"Bravo ! Trouve en {tentatives} tentative(s).")
        break
    elif proposition > secret:
        print("Trop grand")
    else:
        print("Trop petit")
else:
    print(f"Perdu ! Le nombre secret etait {secret}.")
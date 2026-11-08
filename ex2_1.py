
a = float(input("a : "))
b = float(input("b : "))
c = float(input("c : "))

if a == 0:
    
    if b == 0:
        if c == 0:
            print("Equation indeterminee : tout x est solution.")
        else:
            print("Equation impossible : aucune solution.")
    else:
        x = -c / b + 0.0  
        print(f"Equation du 1er degre : x = {x:.2f}")
else:
    delta = b ** 2 - 4 * a * c
    if delta > 0:
        x1 = (-b + delta ** 0.5) / (2 * a)
        x2 = (-b - delta ** 0.5) / (2 * a)
        print(f"Delta = {delta:g} -> x1 = {x1:.2f} ; x2 = {x2:.2f}")
    elif delta == 0:
        x = -b / (2 * a) + 0.0
        print(f"Delta = {delta:g} -> Solution double : x = {x:.2f}")
    else:
        print(f"Delta = {delta:g} -> Pas de solution reelle")


cotes = input("Cotes : ").split()
a = float(cotes[0])
b = float(cotes[1])
c = float(cotes[2])


if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
    print("Ces longueurs ne forment pas un triangle.")
else:
    
    if a == b == c:
        nature = "equilateral"
    elif a == b or b == c or a == c:
        nature = "isocele"
    else:
        nature = "quelconque"

    
    rectangle = (abs(a ** 2 + b ** 2 - c ** 2) < 1e-9
                 or abs(a ** 2 + c ** 2 - b ** 2) < 1e-9
                 or abs(b ** 2 + c ** 2 - a ** 2) < 1e-9)

    message = f"Triangle {nature}"
    if rectangle:
        message += ", rectangle"
    print(message)

a = int(input("a = "))
b = int(input("b = "))
while a <= 0 or b <= 0:
    print("  Les deux entiers doivent etre strictement positifs.")
    a = int(input("a = "))
    b = int(input("b = "))

a_initial, b_initial = a, b  
while b != 0:
    a, b = b, a % b
pgcd = a
ppcm = a_initial * b_initial // pgcd

print(f"a = {a_initial} ; b = {b_initial} -> PGCD = {pgcd} ; PPCM = {ppcm}")

divisions_v1 = 0
print("Version 1 :")
for n in range(2, 51):
    for d in range(2, n):
        divisions_v1 += 1
        if n % d == 0:
            break           
    else:
        print(n, end=" ")   
print()
divisions_v2 = 0
print("Version 2 :")
for n in range(2, 51):
    for d in range(2, int(n ** 0.5) + 1):
        divisions_v2 += 1
        if n % d == 0:
            break
    else:
        print(n, end=" ")
print()
print(f"Divisions effectuees : version 1 = {divisions_v1} ; version 2 = {divisions_v2}")

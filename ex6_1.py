
h = int(input("Hauteur h : "))

print(f"Triangle (h = {h})")
for i in range(1, h + 1):
    for j in range(i):
        print("*", end="")
    print()

print(f"\nPyramide (h = {h})")
for i in range(1, h + 1):
    for j in range(h - i):          
        print(" ", end="")
    for j in range(2 * i - 1):      
        print("*", end="")
    print()

print(f"\nCarre creux (h = {h})")
for i in range(h):
    for j in range(h):
        
        if i == 0 or i == h - 1 or j == 0 or j == h - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

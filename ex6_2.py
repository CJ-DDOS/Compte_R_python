print("  x |", end="")
for j in range(1, 10):
    print(f"{j:3}", end="")
print()
print("----+" + "-" * 30)

for i in range(1, 10):
    print(f"{i:3} |", end="")
    for j in range(1, 10):
        print(f"{i * j:3}", end="")
    print()

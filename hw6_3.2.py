# START

star = "*"
x: int = int(input("Enter number: "))
for i in range(1, x + 1, 2):
    for j in range(i, x + 1):
        print(" ", end="")
    for j in range(1, i + 1):
        print(f"{star:^2}", end="")
    print()

# STOP

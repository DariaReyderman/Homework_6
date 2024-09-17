# START

x: int = int(input("Enter a number > 0: "))
for i in range(1, x + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()
for i in range(x + 1, 1, -1):
    for j in range(1, i - 1):
        print(j, end="")
    print()

# STOP

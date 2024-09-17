# START

import random

x: int = random.randint(1, 100)
print(x)
y: int = int(input("Enter a number: "))
attempts: int = 0
while x != y:
    if y < x:
        print("Your number is too small :( ")
        attempts += 1
        y: int = int(input("Enter a number: "))
    elif y > x:
        print("Your number is too big :( ")
        attempts += 1
        y: int = int(input("Enter a number: "))
else:
    print(f"BINGO!!! Attempts: {attempts}")

# STOP

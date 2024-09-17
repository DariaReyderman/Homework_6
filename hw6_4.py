# START

x: int = int(input("Enter a number: "))
counter: int = 0
while x % 7 == 0:
    counter += 1
    x: int = int(input("Enter a number: "))
    if x % 11 == 0:
        break
else:
    print(counter)

# STOP

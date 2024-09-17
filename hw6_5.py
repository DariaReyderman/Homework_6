# START

x: int = int(input("Enter a number: "))

if x % 5 == 0 and x % 3 == 0:
    print("FizzBuzz")
elif x % 5 == 0:
    print("Fizz")
elif x % 3 == 0:
    print("Buzz")

else:
    print("Try again")

# STOP

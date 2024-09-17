# START

sum_temp: float = 0.0
temp: float = 0.0
for _ in range(5):
    temperature: float = float(input("Enter a temperature in your city: "))
    if temperature < -50 or temperature > 45:
        print("You can do it better...")
        break
    sum_temp += temperature
else:
    avg: float = sum_temp / 5
    print(f"The average temperature in 5 cities is {avg}")

# STOP

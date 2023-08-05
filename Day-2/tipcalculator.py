print("Welcome to the tip calculator")

cost = float(input("What was the total bill? $"))
tip_percent = int(input("What percentage tip you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

calculate = (cost + (cost*(tip_percent/100)))/people

print(f"Each person should pay: ${round(calculate, 2)}")
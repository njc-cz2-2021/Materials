# Assignment 1
num = int(input("Please enter an integer between 1 and 12 inclusive: "))
print(f"Multiples of {num}:")
for i in range(1, 13):
    print(num * i)


print("\n")
# Assignment 2
ten_cents = int(input("Please enter the number of 10-cent coins inserted: "))
twenty_cents = int(input("Please enter the number of 20-cent coins inserted: "))
fifty_cents = int(input("Please enter the number of 50-cent coins inserted: "))
one_dollars = int(input("Please enter the number of 1-dollar coins inserted: "))
cost = float(input("Please enter the price of the drink, e.g., $0.80 or $1.20: ").strip("$"))

change = ten_cents * 10 + twenty_cents * 20 + fifty_cents * 50 + one_dollars * 100 - int(cost * 100)
print("The total change is ${:.2f} in the form of:".format(change / 100))

one_dollars_change = change // 100
print(f"{one_dollars_change} 1-dollar coin" + (change >= 200 or change < 100) * "s")
change -= one_dollars_change * 100

fifty_cents_change = change // 50
print(f"{fifty_cents_change} 50-cent coin" + (change < 50) * "s")
change -= fifty_cents_change * 50

twenty_cents_change = change // 20
print(f"{twenty_cents_change} 20-cent coin" + (change >= 40 or change < 20) * "s")
change -= twenty_cents_change * 20

ten_cents_change = change // 10
print(f"{ten_cents_change} 10-cent coin" + (change < 10) * "s")


print("\n")
# Assignment 3
print("Qaflan will receive", sum(2 ** i for i in range(64)), "grains of wheat.")

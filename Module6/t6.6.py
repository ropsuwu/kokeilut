import math

dcmeter1 = float(input("Enter the diameter of the first pizza (cm): "))
pp1 = float(input("Enter the price of the first pizza (euros): "))
dcmeter2 = float(input("Enter the diameter of the second pizza (cm): "))
pp2 = float(input("Enter the price of the second pizza (euros): "))


def calculate_unit_price(dcmeter, ppe):
    dmeter = dcmeter / 100
    am2 = math.pi * (dmeter / 2) ** 2
    unitprice = ppe / am2
    return unitprice


unitp1 = calculate_unit_price(dcmeter1, pp1)
unitp2 = calculate_unit_price(dcmeter2, pp2)

print(f"Unit price of the first pizza: {unitp1:.2f} euros/m²")
print(f"Unit price of the second pizza: {unitp2:.2f} euros/m²")

if unitp1 < unitp2:
    print("The first pizza provides better value for money.")
elif unitp2 < unitp1:
    print("The second pizza provides better value for money.")

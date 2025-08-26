tuuma = float(input("Enter length in inches (negative value to quit): "))
while tuuma >= 0:
    cm = float(tuuma) * 2.54
    (print(f"{tuuma} inches is {cm:.2f} centimeters"))
    tuuma = float(input("Enter length in inches (negative value to quit): "))
else:
    print("Program ended.")


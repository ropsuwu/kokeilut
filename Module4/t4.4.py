import random

arvaus = int(input("Arvaus: "))
rn = random.randint(1, 10)
while arvaus != rn:
    if arvaus > rn:
        print("Too high")
        arvaus = int(input("Arvaus: "))
    elif arvaus < rn:
        print("Too low")
        arvaus = int(input("Arvaus: "))

print("Correct")

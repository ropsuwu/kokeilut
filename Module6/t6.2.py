import random

side = int(input("Anna tahkojen määrä: "))


def roll_dice(side):
    return random.randint(1, side)


heitto = roll_dice(side)
while heitto != side:
    print(heitto)
    heitto = roll_dice(side)

print(heitto)

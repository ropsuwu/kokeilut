import random


def roll_dice():
    return random.randint(1, 6)


heitto = roll_dice()
while heitto != 6:
    print(heitto)
    heitto = roll_dice()

print(heitto)

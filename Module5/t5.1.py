import random
die=[]
ns = int(input("Anna noppien määrä niin heitän ne sinulle ja kerron summan :"))
for dies in range(ns):
    die.append(random.randint(1,6))
dsum = sum(die)
print(die)
print(dsum)
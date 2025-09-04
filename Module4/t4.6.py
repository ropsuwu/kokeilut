import random
import math

N = int(input("Anna pisteiden määrä: "))

symp = 0
määrä = 0

while määrä < N:
    x = random.uniform(-1,1)
    y = random.uniform(-1,1)

    if x**2 + y**2 < 1:
        symp += 1
    määrä += 1

apie = 4 * symp / N

print(f"About from {math.pi:.2f} {N} has an approximation of {apie}")

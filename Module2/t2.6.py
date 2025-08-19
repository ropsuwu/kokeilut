import random
from timeit import repeat

from Tools.scripts.var_access_benchmark import loop_overhead

#2.6.1. tehtävä 3 satunnaista numero koodi
rng = random.randint(0,9)
rng2 = random.randint(0,9)
rng3 = random.randint(0,9)

#2.6.2. tehtävä 4 satunnaista numero koodi
fng = random.randint(1,6)
fng2 = random.randint(1,6)
fng3 = random.randint(1,6)
fng4 = random.randint(1,6)

print("Kolminumeroinen koodisi on : ", rng, rng2, rng3,"\nNelinumeroinen koodisi on : ",fng, fng2, fng3, fng4)

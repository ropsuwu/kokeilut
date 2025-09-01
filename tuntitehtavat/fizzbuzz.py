nlist = list(range (0,101))
for each in nlist:
    if each % 5 ==0 and each % 3 == 0:
        print("fizzbuzz")
    elif each % 5 == 0:
        print("buzz")
    elif each % 3 == 0:
        print("fizz")
    else:
        print(nlist[each])
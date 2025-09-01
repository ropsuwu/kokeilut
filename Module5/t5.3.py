nb = int(input("Enter an integer: "))

if nb > 1:
    for i in range(2, nb):
        if nb % i == 0:
            print(f"{nb} is not a prime number.")
            break
    else:
        print(f"{nb} is a prime number.")
else:
    print(f"{nb} is not a prime number.")

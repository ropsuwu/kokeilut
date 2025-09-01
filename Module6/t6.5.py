numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []

def filter_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            even.append(number)
filter_even_numbers(numbers)

print(f"Original list: {numbers}")
print(f"List with even numbers only: {even}")

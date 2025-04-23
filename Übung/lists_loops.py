x = 5
y = 10

numbers = [x, y, 15, 20]

for number in numbers:
    print(number)
    number + 5

incremented_numbers = [n + 1 for n in numbers if n >= 10]
print(f"Incremented numbers: {incremented_numbers}")

incremented_numbers = []

for n in numbers:
    if n >= 10:
        incremented_numbers.append(n + 1)
    
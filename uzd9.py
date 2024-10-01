name = input("izdoma vardu ")
letter = input("izdoma burtu ")
amount = 0
for x in name:
    if x == letter:
        amount += 1
print(amount)
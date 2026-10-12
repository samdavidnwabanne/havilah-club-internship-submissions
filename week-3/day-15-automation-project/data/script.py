# A small practice script: prints the multiplication table of a number

number = 7

print("Multiplication table of", number)
for multiplier in range(1, 13):
    print(number, "x", multiplier, "=", number * multiplier)

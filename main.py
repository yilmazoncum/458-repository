binary = input("Enter a binary number: ")
decimal = 0
power = len(binary) - 1

for digit in binary:
    decimal += int(digit) * 2 ** power
    power -= 1

print("The decimal equivalent of", binary, "is", decimal)
n = int(input("Enter a number: "))

binary = bin(n)[2:]

count = 0

for digit in binary:
    if digit == '1':
        count += 1

print("Number of 1 Bits:", count)
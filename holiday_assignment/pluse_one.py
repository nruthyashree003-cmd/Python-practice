digits = list(map(int, input("Enter digits separated by spaces: ").split()))

for i in range(len(digits) - 1, -1, -1):

    if digits[i] < 9:
        digits[i] += 1
        break
    else:
        digits[i] = 0

else:
    digits.insert(0, 1)

print("Result:", digits)
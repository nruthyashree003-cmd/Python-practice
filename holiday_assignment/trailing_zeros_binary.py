n = int(input("Enter a number: "))

count = 0

while n > 0 and n % 2 == 0:
    count += 1
    n = n // 2

print("Trailing zeros:", count)
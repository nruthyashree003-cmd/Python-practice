a, b = map(int, input("Enter a and b: ").split())

total = 0

for i in range(a, b + 1):
    total = total + i ** 3

print("Sum of cubes:", total)
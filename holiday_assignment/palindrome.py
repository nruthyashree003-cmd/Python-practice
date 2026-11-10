
m = int(input("Enter starting number: "))
n = int(input("Enter ending number: "))

result = []

for num in range(m, n + 1):
    if str(num) == str(num)[::-1]:
        result.append(num)

print(result)

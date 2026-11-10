k = int(input("Enter number of lists: "))

lists = []

for i in range(k):
    nums = list(map(int, input("Enter elements: ").split()))
    lists.append(nums)

result = []

for lst in lists:
    result.extend(lst)

result.sort()

print(result)

nums = list(map(int, input("Enter array elements: ").split()))

result = 0

for num in nums:
    result = result ^ num

print("Single Number:", result)

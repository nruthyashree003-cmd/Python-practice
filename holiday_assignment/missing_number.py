
nums =list(map(int, input("enter numbers").split()))

n = len(nums)

expected_sum = n * (n + 1) // 2

actual_sum = sum(nums)

missing_number = expected_sum - actual_sum

print("Missing Number:", missing_number)
# print(len(nums))
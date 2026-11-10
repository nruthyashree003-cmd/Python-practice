nums = list(map(int, input("Enter numbers separated by spaces: ").split()))

max_product = nums[0]
min_product = nums[0]
result = nums[0]

for i in range(1, len(nums)):

    if nums[i] < 0:
        max_product, min_product = min_product, max_product

    max_product = max(nums[i], max_product * nums[i])
    min_product = min(nums[i], min_product * nums[i])   #min store min product at that current position

    result = max(result, max_product)
    # result2 = min(result, min_product)

print("Maximum Product:", result)
# print("Minimum Product:", result2)
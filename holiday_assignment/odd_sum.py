def sum_odd(nums):
    total = 0

    for num in nums:
        if num % 2 != 0:
            total += num

    return total


nums = list(map(int, input("Enter numbers: ").split()))

print("Sum of odd numbers:", sum_odd(nums))
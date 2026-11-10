def filter_decorator(func):

    def wrapper(nums):
        result = func(nums)
        return result

    return wrapper


@filter_decorator
def remove_greater_than_20(nums):
    result = list(filter(lambda x: x <= 20, nums))
    return result


nums = list(map(int, input("Enter numbers: ").split()))

filtered_list = remove_greater_than_20(nums)

print(filtered_list)
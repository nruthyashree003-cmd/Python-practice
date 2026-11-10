def calculate_average():
    numbers = []
    total = 0

    def add_number(num):
        nonlocal total

        numbers.append(num)
        total += num

        average = total / len(numbers)
        print("Cumulative Average:", average)

    return add_number


add = calculate_average()

n = int(input("How many numbers"))

for i in range(n):
    num = int(input("Enter number: "))
    add(num)
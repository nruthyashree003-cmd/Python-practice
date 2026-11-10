l = list(map(int, input("Enter list elements: ").split()))

non_zero = [x for x in l if x != 0]

zeros = [x for x in l if x == 0]

result = non_zero + zeros

print(result)

triplets = [
    [2, 5, 3],
    [1, 8, 4],
    [1, 7, 5]
]

target = [2, 7, 5]

a = False
b = False
c = False

for t in triplets:

    if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
        continue

    if t[0] == target[0]:
        a = True

    if t[1] == target[1]:
        b = True

    if t[2] == target[2]:
        c = True

if a and b and c:
    print("True")
else:
    print("False")


from itertools import combinations

L, K = map(int, input("Enter L and K: ").split())

results = []

# Generate all possible positions for K ones
for positions in combinations(range(L), K):

    binary = ['0'] * L

    for pos in positions:
        binary[pos] = '1'

    s = ''.join(binary)

    # Find maximum consecutive zeros
    count = 0
    max_zero = 0

    for ch in s:
        if ch == '0':
            count += 1
            max_zero = max(max_zero, count)
        else:
            count = 0

    results.append((s, max_zero))


# Print all possible strings
print("\nPossible Strings:")

for s, zeros in results:
    print(s, "-> max zeros =", zeros)


# Find minimum longest zero block
minimum = min(zeros for s, zeros in results)

# Find optimal arrangements
print("\nOptimal Arrangement(s):")

optimal = []

for s, zeros in results:
    if zeros == minimum:
        optimal.append(s)

print(", ".join(optimal))

print("Minimum Longest Zero Block:", minimum)

def climb_stairs(n):

    patterns = []

    def find_ways(remaining, path):

        if remaining == 0:
            patterns.append(path)
            return

        if remaining >= 1:
            find_ways(remaining - 1, path + [1])

        if remaining >= 2:
            find_ways(remaining - 2, path + [2])

    find_ways(n, [])

    print("Total Ways:", len(patterns))
    print("Patterns:")

    for pattern in patterns:
        print("+".join(map(str, pattern)))


n = int(input("Enter number of steps: "))
climb_stairs(n)
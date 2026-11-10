def matrix_chain(dims):

    n = len(dims) - 1

    dp = [[0] * (n + 1) for _ in range(n + 1)]
    split = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):

        for i in range(1, n - length + 2):

            j = i + length - 1
            dp[i][j] = float('inf')

            for k in range(i, j):

                cost = (dp[i][k] + dp[k+1][j]
                        + dims[i-1] * dims[k] * dims[j])

                if cost < dp[i][j]:
                    dp[i][j] = cost
                    split[i][j] = k

    def parenthesization(i, j):

        if i == j:
            return "A" + str(i)

        k = split[i][j]

        left = parenthesization(i, k)
        right = parenthesization(k+1, j)

        return "(" + left + " x " + right + ")"

    def print_steps(i, j):

        if i == j:
            return

        k = split[i][j]

        print_steps(i, k)
        print_steps(k+1, j)

        cost = dims[i-1] * dims[k] * dims[j]

        print("Multiply", parenthesization(i, j),
              "-> Cost:", cost)

    print("Minimum Cost:", dp[1][n])

    print("Optimal Parenthesization:",
          parenthesization(1, n))

    print("Multiplication Sequence:")
    print_steps(1, n)


dims = list(map(int, input("Enter dimensions: ").split()))

matrix_chain(dims)
def solve_maze(maze, n):
    solution = [[0 for j in range(n)] for i in range(n)]

    def is_safe(x, y):
        return (x >= 0 and x < n and
                y >= 0 and y < n and
                maze[x][y] == 1 and
                solution[x][y] == 0)

    def find_path(x, y):

        # Destination reached
        if x == n - 1 and y == n - 1:
            solution[x][y] = 1
            return True

        if is_safe(x, y):

            # Mark current cell
            solution[x][y] = 1

            # Move Down
            if find_path(x + 1, y):
                return True

            # Move Right
            if find_path(x, y + 1):
                return True

            # Move Up
            if find_path(x - 1, y):
                return True

            # Move Left
            if find_path(x, y - 1):
                return True

            # Backtrack
            solution[x][y] = 0

        return False

    if maze[0][0] == 0 or maze[n-1][n-1] == 0:
        print("No solution exists")
        return

    if find_path(0, 0):
        print("Solution Path:")
        for row in solution:
            print("".join(map(str, row)))
    else:
        print("No solution exists")


# Main program
n = 4

maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

solve_maze(maze, n)
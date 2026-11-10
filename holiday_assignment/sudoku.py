def is_valid(board, row, col, num):

    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Find starting position of 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3

    # Check 3x3 box
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True


def validate(board):

    for i in range(9):
        for j in range(9):

            num = board[i][j]

            if num != '.':
                board[i][j] = '.'

                if not is_valid(board, i, j, num):
                    board[i][j] = num
                    return False

                board[i][j] = num

    return True


def solve(board):

    for i in range(9):
        for j in range(9):

            if board[i][j] == '.':

                for num in '123456789':

                    if is_valid(board, i, j, num):

                        board[i][j] = num

                        if solve(board):
                            return True

                        board[i][j] = '.'

                return False

    return True


# Take input
board = []

print("Enter the Sudoku board (use . for empty cells):")

for i in range(9):
    row = input().split()
    board.append(row)


if validate(board):
    print("Valid Sudoku: True")

    if solve(board):
        print("Completed Sudoku:")

        for i in range(9):
            print(" ".join(board[i][:3]), "|",
                  " ".join(board[i][3:6]), "|",
                  " ".join(board[i][6:]))

            if i == 2 or i == 5:
                print("-" * 25)

else:
    print("Invalid Sudoku: False")
    print("Reason: Duplicate number in a row, column, or 3x3 box.")
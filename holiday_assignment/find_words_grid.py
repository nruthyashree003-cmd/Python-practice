class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None


def findWords(board, words):

    root = TrieNode()

    # Step 1: Build Trie
    for word in words:
        node = root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()

            node = node.children[ch]

        node.word = word

    result = []

    rows = len(board)
    cols = len(board[0])

    # Step 2: DFS
    def dfs(r, c, node):

        ch = board[r][c]

        if ch not in node.children:
            return

        node = node.children[ch]

        # Complete word found
        if node.word is not None:
            result.append(node.word)
            node.word = None

        # Mark cell as visited
        board[r][c] = "#"

        # Four directions: down, up, right, left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            if 0 <= nr < rows and 0 <= nc < cols:
                if board[nr][nc] != "#":
                    dfs(nr, nc, node)

        # Restore original character
        board[r][c] = ch

    # Step 3: Start DFS from every cell
    for i in range(rows):
        for j in range(cols):
            dfs(i, j, root)

    return result


# Take input from user
m, n = map(int, input("Enter rows and columns: ").split())

board = []

print("Enter the grid rows:")
for i in range(m):
    row = input().split()
    board.append(row)

count = int(input("Enter number of words: "))

words = []

print("Enter the words:")
for i in range(count):
    words.append(input())

answer = findWords(board, words)

print("Words found:", answer)
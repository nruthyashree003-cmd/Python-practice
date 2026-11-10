class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def invert(root):
    if root is None:
        return None

    root.left, root.right = root.right, root.left

    invert(root.left)
    invert(root.right)

    return root


def print_tree(root):
    if root is None:
        return

    queue = [root]

    while queue:
        current = queue.pop(0)
        print(current.data, end=" ")

        if current.left:
            queue.append(current.left)

        if current.right:
            queue.append(current.right)


# Taking input
values = list(map(int, input("Enter tree values: ").split()))

# Creating the binary tree
root = Node(values[0])
queue = [root]
i = 1

while i < len(values):
    current = queue.pop(0)

    current.left = Node(values[i])
    queue.append(current.left)
    i += 1

    if i < len(values):
        current.right = Node(values[i])
        queue.append(current.right)
        i += 1

# Inverting the tree
invert(root)

print("Inverted Tree:")
print_tree(root)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def kthSmallest(root, k):
    result = []

    def inorder(node):
        if node is None:
            return

        inorder(node.left)
        result.append(node.val)
        inorder(node.right)

    inorder(root)

    return result[k - 1]


# Creating the BST
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)

root.left.left = TreeNode(1)
root.left.right = TreeNode(6)

root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)

root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

# Taking k as input
k = int(input("Enter the value of k: "))

# Finding kth smallest element
answer = kthSmallest(root, k)

print(f"{k}th smallest element =", answer)

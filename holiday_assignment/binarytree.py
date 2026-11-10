
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):

    def height(node):
        if node is None:
            return 0

        left = height(node.left)
        right = height(node.right)

        if left == -1 or right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return max(left, right) + 1

    return height(root) != -1


# tree  3, 9, 20, NULL, NULL, 15, 7
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

print(isBalanced(root))

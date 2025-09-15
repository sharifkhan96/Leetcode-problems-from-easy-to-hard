class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        # Base case: if the node is None, no path exists
        if not root:
            return False

        # Subtract current node's value from target
        targetSum -= root.val

        # If this is a leaf node, check if the targetSum is 0
        if not root.left and not root.right:
            return targetSum == 0

        # Otherwise, check left or right subtree
        return (self.hasPathSum(root.left, targetSum) or
                self.hasPathSum(root.right, targetSum))


def main():
    # Example 1
    # Tree:
    #       5
    #      / \
    #     4   8
    #    /   / \
    #   11  13  4
    #  /  \      \
    # 7    2      1
    #
    # Target = 22
    #
    # Valid path = 5 -> 4 -> 11 -> 2 (sum = 22)

    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)

    target = 22

    solution = Solution()
    print("Does a path exist with sum =", target, "? ->",
          solution.hasPathSum(root, target))

    # Example 2 (no valid path)
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    target2 = 5
    print("Does a path exist with sum =", target2, "? ->",
          solution.hasPathSum(root2, target2))


if __name__ == "__main__":
    main()

# definition of a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # base case: empty subtree has depth 0
        if not root:
            return 0

        # here, wecursively compute left and right subtree depths
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)

        # our current node contributes 1 + max of child depths
        return 1 + max(left_depth, right_depth)


def main():
    # drwan by chatgpt :)))) but i did contributed to the code though
    # Build example tree:
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    solution = Solution()
    depth = solution.maxDepth(root)
    print("Maximum Depth of Tree:", depth)  # Expected output: 3


if __name__ == "__main__":
    main()

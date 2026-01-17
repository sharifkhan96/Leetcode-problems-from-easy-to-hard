class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root) -> int:
        # recursive solution
        self.diatmeter = 0

        def depth(root):
            if not root:
                return 0
            
            left_depth = depth(root.left)
            right_depth = depth(root.right)

            self.diameter = max(self.diatmeter + left_depth + right_depth)

            return 1 + max(left_depth, right_depth)
        
        depth(root)
        return self.diatmeter


def main():

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()
    
    print(solution.diameterOfBinaryTree(root))


if __name__ == "__main__":
    main()

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p q) -> 'TreeNode':
        if not root:
            return None

        # If we find p or q, return it upward (a node can be a descendant of itself)
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # If p and q are found in different subtrees, root is the LCA
        if left and right:
            return root

        # Otherwise, return whichever side found p or q (or None)
        return left if left else right



def main():

    #root = [3,5,1,6,2,0,8,null,null,7,4],

    root = Solution(3)
    root.left = Solution(5)
    root.right = Solution(1)

    p = 5
    q = 1
    solution = Solution()
    solution.lowestCommonAncestor(root, p, q)


if __name__ == "__main__":
    main()

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q) -> 'TreeNode':
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

# time and space complexity: O(N) & O(H) where H is the height of the tree 


def main():

    root = TreeNode(3)
    #root.left = TreeNode(5)
    #root.right = TreeNode(1)
    node5 = TreeNode(5)
    node1 = TreeNode(1)

    root.left = node5
    root.right = node1

    p = node5
    q = node1
    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)
    print(lca.val)



if __name__ == "__main__":
    main()

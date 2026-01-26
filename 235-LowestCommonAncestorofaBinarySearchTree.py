# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        # small = min(p.val, q.val)
        # large = max(p.val, q.val)

        # while root:
        #     if root.val > large:
        #         root = root.left
        #     elif root.val < small:
        #         root = root.right
        #     else:
        #         return root
        # return None


        '''
        # recursive solution
        if root is None:
            return None
        
        small = min(p.val, q.val)
        large = max(p.val, q.val)

        if root.val > large:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < small:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root
        
        
        Time: O(h) where h is tree height
        balanced: O(log n)
        worst (skewed): O(n)
        Space: O(h) due to recursion stack
        '''



def main():
    
    root = TreeNode(3)
    #root.left = TreeNode(5)
    #root.right = TreeNode(1)
    node1 = TreeNode(1)
    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node6 = TreeNode(6)

    root.left = node1
    root.right = node5

    root.right.left = node4
    root.right.right = node6

    p = node4
    q = node6

    solution = Solution()
    lca = solution.lowestCommonAncestor(root, p, q)
    print(lca.val)



if __name__ == "__main__":
    main()

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:

        # iterative solution: 
        # time & space complexities: O(N) & O(H), worst case O(N) respectively
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in (node1, node2) or node1.val != node2.val:
                return False

            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))

        return True


        '''
        # recursive solutionnnnnnn
        
        # Case 1: both are None → same
        if not p and not q:
            return True
        
        # Case 2: one is None, other is not → different
        if not p or not q:
            return False
        
        # Case 3: values differ → different
        if p.val != q.val:
            return False
        
        # Case 4: check left subtree and right subtree recursively
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        '''
        


def main():
    # Example 1: identical trees
    # Tree p
    p = TreeNode(1)
    p.left = TreeNode(2)
    p.right = TreeNode(3)

    # Tree q
    q = TreeNode(1)
    q.left = TreeNode(2)
    q.right = TreeNode(3)

    solution = Solution()
    print("Are the trees the same? ->", solution.isSameTree(p, q))  # True

    # Example 2: different trees
    p2 = TreeNode(1)
    p2.left = TreeNode(2)

    q2 = TreeNode(1)
    q2.right = TreeNode(2)

    print("Are the trees the same? ->", solution.isSameTree(p2, q2))  # False


if __name__ == "__main__":
    main()
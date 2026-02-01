
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        # iterative solution: O(H + k) & O(H)
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            k -= 1
            if not k:
                return root.val
            root = root.right
        
        # recursive solution 
        # def Inorder(root: Optional[TreeNode]) -> int:
        #     return Inorder(root.left) + [root.val] + Inorder(root.right) if root else []

        # return Inorder(root=root)[k - 1]

# time and space complexities: O(n) fro traversing and O(n) for stroing bst values in the array

def main():
    
    root = TreeNode(3)
    #root.left = TreeNode(5)
    #root.right = TreeNode(1)
    node1 = TreeNode(1)
    node4 = TreeNode(4)
    node2 = TreeNode(2)


    root.left = node1
    root.right = node4

    root.left.right = node2

    solution = Solution()
    print(solution.kthSmallest(root=root, k=1))


    # time adn space compleities: O(N) & O(N)


if __name__ == "__main__":
    main()

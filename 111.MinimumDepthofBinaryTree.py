# Definition for a binary tree node.
# Definition for a binary tree node.

from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root) -> int:
        if not root:
            return 0
        
        queue = deque([root], 1) # node and depth

        while queue:
            node, depth = queue.popleft()
            if not node.left and not node.right:
                return depth
            
            if node.left:
                queue.append((node.left, depth + 1))
            if node.right:
                queue.append((node.right, depth + 1))

        



    
def main():
    
    root = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)

    root.left = node9
    root.right = node20
    node20.left = node15
    node20.right = node7

    obj = Solution()
    print(obj.minDepth(root))

    


if __name__ == "__main__":
    main()
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False

            if k - node.val in seen:
                return True
            
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
        
# Time: O(n)
# Space: O(n) (hash set + recursion stack)

def main():
    
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.right.right = TreeNode(7)

    val = 9
    obj = Solution()
    
    result = obj.findTarget(root, val)
    
    if result:
         print(f"{result}, {val} has two adder values")
    else:
         print("Oppps, {result}, {val} Doens not have adder values")


if __name__ == "__main__":
    main()
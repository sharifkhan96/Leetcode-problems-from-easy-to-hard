from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # two line recursive soluiotn
        # time and space complexity: O(log n) & O(h) where H is the height of the tree 
        # if root is None or root.val == val:
        #     return root
        
        # return self.searchBST(root.left, val) if val < root.val \
        #     else self.searchBST(root.right, val)
    

        # iteraive solution:
        while root:
            if root.val == val:
                return root
            
            root = root.left if val < root.val else root.right
        return None



def main():
    
    root = TreeNode(3)
    #root.left = TreeNode(5)
    #root.right = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
 
    val = 5
    obj = Solution()
    result = obj.searchBST(root, val)
    
    if result:
        print(result.val)
    else:
        print("Valeu not found")



if __name__ == "__main__":
    main()

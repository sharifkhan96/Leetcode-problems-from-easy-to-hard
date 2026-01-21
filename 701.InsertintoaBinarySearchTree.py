from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
     def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
            # recursive sol: time and space complexeities: O(log n) & O(log n)
            # if root is None:
            #      return TreeNode(val)
            
            # if val < root.val:
            #      root.left = self.insertIntoBST(root.left, val)
            # elif val > root.val:
            #      root.right = self.insertIntoBST(root.right, val)

            # return root
     
            # iterative soltion: time & space complexities: O(log n) & O(1)
            node = root
            while node:
                if val < node.val:
                    if not node.left:
                        node.left = TreeNode(val)
                        return root
                    else:
                        node = node.left

                else:
                     if not node.right:
                            node.right = TreeNode(val)
                            return root
                     else:
                            node = node.right
            return TreeNode(val)
                     

     # this leetcode problem is jsut a helper function here..
     def searchBST(self, root: Optional[TreeNode], value: int)-> Optional[TreeNode]:
            if root is None or root.val == value:
                 return root
            
            return self.searchBST(root.left, value) if value < root.val \
                else self.searchBST(root.right, value)
     
            # iteraive solution:
            # while root:
            #     if root.val == val:
            #         return root
                
            #     root = root.left if val < root.val else root.right
            # return None



def main():
    
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)

    val = 5
    obj = Solution()
    
    result = obj.searchBST(root, val)
    
    if result:
         print(f"{result.val} inserted successfully.")
    else:
         print("Oppps, {val} not inserted.")

    new_root = obj.insertIntoBST(root, val)

    result = obj.searchBST(new_root, val)
    
    if result:
         print(f"{result.val} inserted successfully.")
    else:
         print("Oppps, value not inserted.")



if __name__ == "__main__":
    main()

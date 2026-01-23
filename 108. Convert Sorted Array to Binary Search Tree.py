from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(left, right):
            if left > right:
                return None

            p = (left + right) // 2

            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root
        return helper(0, len(nums) - 1)
                     

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

    def inorder(self, root):
        if not root:
            return []
        return self.inorder(root.left) + [root.val] + self.inorder(root.right)


    def isValidBST(self, root, low=float("-inf"), high=float("inf")):
        if not root:
            return True

        if not (low < root.val < high):
            return False

        return (
            self.isValidBST(root.left, low, root.val) and
            self.isValidBST(root.right, root.val, high)
        )




def main():
    nums = [-10, -3, 0, 5, 9]
    val = 5

    obj = Solution()
    root = obj.sortedArrayToBST(nums)

    # 1. confirming BST via inorder
    print("Inorder traversal:", obj.inorder(root))

    # 2. confirming value exists
    found = obj.searchBST(root, val)
    print("Value found:", found.val if found else "Not found")

    # 3. validdating BST formally
    print("Is valid BST:", obj.isValidBST(root))



if __name__ == "__main__":
    main()

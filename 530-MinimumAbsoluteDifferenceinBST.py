from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
# in order traversal using list
        # inOrderNodes = []

        # def inOrder(node):
        #     if node is None:
        #         return
            
        #     inOrder(node.left)
        #     inOrderNodes.append(node.val)
        #     inOrder(node.right)
            
        # inOrder(root)
        # minDiff = float('inf')
        # for i in range(1, len(inOrderNodes)):
        #     minDiff = min(minDiff, inOrderNodes[i] - inOrderNodes[i - 1])
        
        # return minDiff

        # in order traversal without the list
        self.mindiff = float('inf')
        self.prevNode = None

        def inOrder(node):
            if node is None:
                return 
            
            inOrder(node.left)
            if self.prevNode is not None:
                self.mindiff = min(self.mindiff, node.val - self.prevNode)
            
            self.prevNode = node.val
            inOrder(node.right)

        inOrder(root)
        return self.mindiff

# DFS approach
#         nodeValues = []

#         def dfs(node):
#             if node is None:
#                 return
#             nodeValues.append(node.val)
#             dfs(node.left)
#             dfs(node.right)

#         dfs(root)

#         minDifference = float('inf')
#         nodeValues.sort()
#         for i in range(1, len(nodeValues)):
#             minDifference = min(minDifference, nodeValues[i] - nodeValues[i - 1])
        
#         return minDifference

# # time and space complexities: O(n log n) & O(n)

def main():
    
    root = TreeNode(9)
    #root.left = TreeNode(5)
    #root.right = TreeNode(1)
    node11 = TreeNode(11)
    node7 = TreeNode(7)
    node8 = TreeNode(8)
    node2 = TreeNode(2)

    root.left = node7
    root.right = node11

    root.left.left = node2
    root.left.right = node8

    solution = Solution()
    print("Minimum absolute difference is: ", solution.getMinimumDifference(root))



if __name__ == "__main__":
    main()

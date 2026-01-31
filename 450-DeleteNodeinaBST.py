
from typing import Optional
# definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:

    # recursive solution
    # one node right & then go left deep down
    # def successor(self, root: TreeNode) -> int:
    #     root = root.right
    #     while root.left:
    #         root = root.left
    #     return root.val

    # # one node left & then go right deep down
    # def predecessor(self, root: TreeNode) -> int:
    #     root = root.left
    #     while root.right:
    #         root = root.right
    #     return root.val

    # def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

    #     if not root:
    #         return None

    #     if key > root.val: # delete form the right substree
    #         root.right = self.deleteNode(root.right, key)
    #     elif key < root.val: # delete from the left subtree
    #         root.left = self.deleteNode(root.left, key)
    #     else: # here, we basically delete the current node
    #         # case1: node is a leaf
    #         if not (root.left or root.right):
    #             root = None
    #         elif root.right:
    #             root.val = self.successor(root)
    #             root.right = self.deleteNode(root.right, root.val)
    #         else:
    #             root.val = self.predecessor(root)
    #             root.left = self.deleteNode(root.left, root.val)

    #     return root
# Recursive sol: time and space complexities: O(log n) & O(h or log n)


    # iteratve solution
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return None
        
        parent = None
        currentNode = root
        
        # findng the node to delete
        while currentNode and currentNode.val != key:
            parent = currentNode
            if key < currentNode.val:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        # node to be deleted not found
        if not currentNode:
            return root
        
        # case 1 : node with no children
        if not currentNode.left and not currentNode.right:
            if not parent:
                return None
            if parent.left == currentNode:
                parent.left = None
            else:
                parent.right = None

        # case2 : node with only one child
        elif not currentNode.left or not currentNode.right:
            child = currentNode.left if currentNode.left else currentNode.right
            if not parent:
                return child
            if parent.left == currentNode:
                parent.left = child
            else:
                parent.right = child

        # case 3 : node with 2 children
        else:
            # finding the inorder successor(smallest in the right subtree)
            successor_parent = currentNode
            successor = currentNode.right
            while successor.left:
                successor_parent = successor
                successor = successor.left
            
            # copy the inorder successor's content to the current node
            currentNode.val = successor.val

            # delete the inorder successor
            if successor_parent.left == successor:
                successor_parent.left = successor.right
            else:
                successor_parent.right = successor.right

        return root
    

    def searchBST(self, root, key):
        while root:
            if key == root.val:
                return root
            
            root = root.left if key < root.val else root.right
        return None

    


def main():
    
    root = TreeNode(5)
    #root.left = TreeNode(5)
    #root.right = TreeNode(1)
    node3 = TreeNode(3)
    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node4 = TreeNode(4)
    node7 = TreeNode(7)

    root.left = node3
    root.right = node6
    root.left.left = node2
    root.left.right = node4
    root.right.right = node7

    value1 = 3
    obj = Solution()
    result = obj.searchBST(root, value1)
    
    if result:
        print(f" Value: {result.val} found.")
    else:
        print(f"Valeu {value1} not found")

    solution = Solution()
    newRoot = solution.deleteNode(root, key=3)

    value1 = 3
    obj = Solution()
    result = obj.searchBST(newRoot, value1)
    
    if result:
        print(f" Value: {result.val} found.")
    else:
        print(f"Valeu {value1} not found")


if __name__ == "__main__":
    main()


from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        # Create a list to store the inorder traversal of the BST
        inorder = []
        self.inorder_traversal(root, inorder)

        # Construct and return the balanced BST
        return self.create_balanced_bst(inorder, 0, len(inorder) - 1)

    def inorder_traversal(self, root: TreeNode, inorder: list):
        # Performinggggg an inorder traversal to store the elements in sorted order
        if not root:
            return
        self.inorder_traversal(root.left, inorder)
        inorder.append(root.val)
        self.inorder_traversal(root.right, inorder)


    '''
    instead of inorder_traversal fun, you can just do:
    inorder = []
        def dfs(node):
            if node is None:
                return
            
            inorder.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        inorder.sort()
    '''

    def create_balanced_bst(
        self, inorder: list, start: int, end: int
    ) -> TreeNode:
        # Base case: if the start index is greater than the end index, return None
        if start > end:
            return None

        # here, we gota the middle element of the current range
        mid = start + (end - start) // 2

        # Recursively construct the left and right subtrees
        left_subtree = self.create_balanced_bst(inorder, start, mid - 1)
        right_subtree = self.create_balanced_bst(inorder, mid + 1, end)

        # creating a new node with the middle element and attach the subtrees
        node = TreeNode(inorder[mid], left_subtree, right_subtree)
        return node

# time and space complexities: O(n) fro traversing and O(n) for stroing bst values in the array

def main():
    
    root = TreeNode(1)
    #root.left = TreeNode(5)
    #root.right = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)


    root.right = node2
    root.right.right = node3

    root.right.right.right = node4

    solution = Solution()

    # state = False
    # if root.left:
    #     state = True
    # else:
    #     state = False
    # print(state)

    print("Bfore balancing the BST, root.left exist? ", bool(root.left))
    print("Tree is balance? ", bool(root.left))

    root = solution.balanceBST(root)

    # if root.left:
    #     state = True
    # else:
    #     state = False
    # print(state)
    print("Bfore balancing the BST, root.left exist? ", bool(root.left))
    print("Tree is balance? ", bool(root.left))


if __name__ == "__main__":
    main()

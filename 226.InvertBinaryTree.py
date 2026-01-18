from collections import deque
# print funciton for the tree
def print_tree_level_order(root):
    if not root:
        print([])
        return

    queue = deque([root])
    result = []

    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result.append(level)

    print(result)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
    
        # # recursive solution
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
            return root

        '''
        
        # iterative solution: 
        # time and space complexitties: O(N) and O(N)
        
        stack = [root]

        while stack:

            current_node = stack.pop()

            if current_node:
                current_node.left, current_node.right = current_node.right, current_node.left
                stack.extend([current_node.right, current_node.left])

        return root
        '''


def main():

    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)

    print("Before inversion:")
    print_tree_level_order(root)

    solution = Solution()
    solution.invertTree(root)

    print("After inversion:")
    print_tree_level_order(root)


if __name__ == "__main__":
    main()

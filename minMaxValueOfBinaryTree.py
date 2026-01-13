from collections import deque
# definition of a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def MaxvalueBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return None
        queue = deque()
        queue.append(root)
        # max_node = float("-inf")
        max_node = 0
        while queue:
            current_node = queue.popleft()

            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)

            if current_node.val > max_node:
                max_node = current_node.val

        return max_node



    def MinvalueBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return None
        q = deque([root])
        # min_node = float("inf")
        min_node = root.val
        while q:
            current_node = q.popleft()
            min_node = min(min_node, current_node.val)
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            
        return min_node


def main():
    # drwan by chatgpt :)))) but i did contributed to the code though
    # Build example tree:
    #     3
    #    / \
    #   9  20
    #      / \
    #     15  7

    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    obj = Solution()
    Maxdepth = obj.MaxvalueBinaryTree(root)
    print("Max value of Tree:", Maxdepth)  # expected output: 15

    Mindepth = obj.MinvalueBinaryTree(root)
    print("min value of Tree:", Mindepth)  # expected output: 3


if __name__ == "__main__":
    main()

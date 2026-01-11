from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root) -> list[float]:

        if not root:
            return
        
        queue = deque([root])

        result = []

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sum(level)/len(level))

        return result


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
    print(obj.averageOfLevels(root))   # Expected: [3.0, 14.5, 11.0]

    


if __name__ == "__main__":
    main()
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def averageOfLevels(self, root) -> list[float]:
        queue = deque([root])

        result = []

        while queue:
            level = []
            for i in range(queue):
                node = queue.popleft()
                level.append(node.val)
                if node.left: 
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(sum(level)/len(level))

        return result


def main():
    ...

    


if __name__ == "__main__":
    main()
from collections import deque
# definition of a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:

        # BDF
        if not root:
            return 0
        q = deque()
        q.append(root)
        depth = 0

        while q:
            depth += 1
            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth
        # time & space complexities: O(N) & O(N) respectively
        '''
        # DFS(Depth First Search), the way it works is by going to the depth of each brance and when it touches the leaf
        # it then calculates the depth and camparing it with the depth of the other brance + 1
        # base case: empty subtree has depth 0
        if not root:
            return 0

        # here, wecursively compute left and right subtree depths
        #left_depth = self.maxDepth(root.left)
        #right_depth = self.maxDepth(root.right)

        # our current node contributes 1 + max of child depths
        #return 1 + max(left_depth, right_depth)
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        '''

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

    solution = Solution()
    depth = solution.maxDepth(root)
    print("Maximum Depth of Tree:", depth)  # expected output: 3


if __name__ == "__main__":
    main()

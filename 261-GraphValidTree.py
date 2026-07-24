from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # A valid tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        # Create adjacency list
        graph = [[] for _ in range(n)]

        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = set()

        def dfs(node: int, parent: int) -> bool:
            visited.add(node)

            for neighbor in graph[node]:
                # Do not go directly back to the parent
                if neighbor == parent:
                    continue

                # A visited neighbor that is not the parent means a cycle
                if neighbor in visited:
                    return False

                if not dfs(neighbor, node):
                    return False

            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # All nodes must be connected
        return len(visited) == n


# Time complexity: O(n + e)
# Space complexity: O(n + e)


def main():
    n = 5
    edges = [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4]
    ]

    obj1 = Solution()
    result = obj1.validTree(n, edges)

    print(result)


if __name__ == "__main__":
    main()
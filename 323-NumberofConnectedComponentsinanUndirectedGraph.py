class Solution:

    def countComponents(self, n: int, edges: list[list[int]]) -> int:

        adjList = [[] for _ in range(n)]

        for node1, node2 in edges:
            adjList[node1].append(node2)
            adjList[node2].append(node1)


        counter = 0
        visited = set()

        def dfs(node):
            visited.add(node)

            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # second way of dfs function
        # def dfs(start):
        #     stack = [start]
        #     visited.add(start)
        #     while stack:
        #         node = stack.pop()
        #         for neighbor in adjList[node]:
        #             if neighbor not in visited:
        #                 visited.add(neighbor)
        #                 stack.append(neighbor)

        for node in range(n):
            if node not in visited:
                counter += 1
                dfs(node)

        return counter


def main():
    n = 5
    edges = [[0,1],[1,2],[3,4]]

    obj1 = Solution()

    print(obj1.countComponents(n, edges))


if __name__ == "__main__":
    main()
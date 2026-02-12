from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        visited = [False] * n
        provinces = 0

        def dfs(city):
            visited[city] = True

            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        
        for city in range(n):

            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces


# time and space complexities: O(n^2) and O(n)


def main():
    isConnected = [[1,1,0],[1,1,0],[0,0,1]]

    obj1 = Solution()
    print(obj1.findCircleNum(isConnected))


if __name__ == "__main__":
    main()
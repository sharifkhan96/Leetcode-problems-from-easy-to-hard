from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

# time and space comps:
# time: O(N + M) as we traverse through vertices & edges
# space: O(N) as we store nodes in visited hashmap
class Solution:
    def __init__(self):
        # visited node in the form of dict
        self.visited = {}

    def cloneGraphDFS(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node 

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val, [])

        self.visited[node] = clone_node


        if node.neighbors:
            clone_node.neighbors = [self.cloneGraphDFS(n) for n in node.neighbors]
        
        return clone_node

class main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)

    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]

    sol = Solution()

    cloned = sol.cloneGraphDFS(n4)

    #print(cloned.val)
    print("Neighbors of ", str(cloned.val) + " are: ", [n.val for n in cloned.neighbors])




if __name__ == "__main__":
    main()










'''
BFS solution:
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from collections import deque


class Solution:

    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:

        if not node:
            return node

        # Dictionary to save the visited node and it's respective clone
        # as key and value respectively. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # Add the clone of the neighbor to the neighbors of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]
'''
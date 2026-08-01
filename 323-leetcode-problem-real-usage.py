class ConnectedComponentsRealWorld:
    """Demonstrates 8 real-world applications of finding connected components"""

    def _count_components(self, n: int, edges: list[list[int]]) -> int:
        """Helper: standard connected components algorithm"""
        adjList = [[] for _ in range(n)]
        for u, v in edges:
            adjList[u].append(v)
            adjList[v].append(u)

        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in adjList[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        counter = 0
        for node in range(n):
            if node not in visited:
                counter += 1
                dfs(node)
        return counter

    def social_network_communities(self):
        """Find friend communities in a social network"""
        n_users = 8  # users 0-7
        friendships = [[0, 1], [1, 2], [3, 4], [5, 6], [6, 7]]
        communities = self._count_components(n_users, friendships)

        return {
            "scenario": "Social Network Communities",
            "description": "Finding isolated friend groups",
            "users": n_users,
            "friendships": friendships,
            "result": f"{communities} separate communities detected",
            "use_case": "LinkedIn, Discord, Facebook"
        }

    def network_infrastructure_connectivity(self):
        """Check if data centers are connected"""
        n_servers = 6  # servers 0-5
        connections = [[0, 1], [1, 2], [3, 4]]  # 2 clusters: 0-1-2 and 3-4, server 5 isolated
        clusters = self._count_components(n_servers, connections)

        return {
            "scenario": "Network Infrastructure",
            "description": "Checking data center connectivity",
            "servers": n_servers,
            "connections": connections,
            "result": f"{clusters} isolated network clusters (alert if > 1!)",
            "use_case": "DevOps, Cloud Infrastructure, Monitoring"
        }

    def image_blob_detection(self):
        """Find connected pixel regions in an image"""
        n_pixels = 9  # 3x3 grid as flat array
        adjacent_pixels = [[0, 1], [1, 2], [3, 4], [5, 6], [6, 7], [7, 8]]
        blobs = self._count_components(n_pixels, adjacent_pixels)

        return {
            "scenario": "Image Blob Detection",
            "description": "Finding separate objects in an image",
            "grid": "3x3 pixel grid",
            "connected_pixels": adjacent_pixels,
            "result": f"{blobs} distinct blobs/regions found",
            "use_case": "Medical Imaging, Computer Vision, Photo Processing"
        }

    def game_terrain_connectivity(self):
        """Check if map areas are traversable"""
        n_chunks = 7  # terrain chunks
        walkable_paths = [[0, 1], [1, 2], [2, 3], [4, 5]]  # 3 islands
        islands = self._count_components(n_chunks, walkable_paths)

        return {
            "scenario": "Game Terrain Connectivity",
            "description": "Finding separate traversable map areas",
            "map_chunks": n_chunks,
            "paths": walkable_paths,
            "result": f"{islands} separate island regions (player cannot traverse between them)",
            "use_case": "Game Dev, Level Design, Dungeon Generation"
        }

    def database_deduplication(self):
        """Find clusters of duplicate customer records"""
        n_records = 10  # customer records
        duplicate_links = [[0, 3], [3, 7], [1, 5], [2, 8], [8, 9]]  # groups of same customer
        customer_clusters = self._count_components(n_records, duplicate_links)

        return {
            "scenario": "Database Deduplication",
            "description": "Merging duplicate customer records",
            "records": n_records,
            "linked_duplicates": duplicate_links,
            "result": f"{customer_clusters} unique customers (consolidated from {n_records} records)",
            "use_case": "Data Warehousing, CRM, Entity Resolution"
        }

    def user_clustering_recommendation(self):
        """Cluster users with similar behavior"""
        n_users = 8
        similar_behavior = [[0, 1], [1, 3], [2, 4], [5, 6]]  # behavior groups
        user_clusters = self._count_components(n_users, similar_behavior)

        return {
            "scenario": "User Clustering & Recommendation",
            "description": "Grouping users by similar interests/behavior",
            "users": n_users,
            "similarity_edges": similar_behavior,
            "result": f"{user_clusters} user clusters for targeted recommendations",
            "use_case": "Netflix, Spotify, Amazon Recommendations"
        }

    def dependency_analysis(self):
        """Find tightly coupled modules that must deploy together"""
        n_modules = 9  # software modules
        dependencies = [[0, 1], [1, 2], [3, 4], [5, 6], [6, 7]]  # coupling groups
        deployment_groups = self._count_components(n_modules, dependencies)

        return {
            "scenario": "Dependency Analysis (Microservices)",
            "description": "Finding independent vs coupled service modules",
            "modules": n_modules,
            "coupled_modules": dependencies,
            "result": f"{deployment_groups} independent deployment units",
            "use_case": "Microservices Architecture, CI/CD, Deployment Planning"
        }

    def circuit_validation(self):
        """Verify all components in a circuit are connected"""
        n_components = 6  # resistors, capacitors, etc.
        wired_connections = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5]]  # all connected in series
        circuit_groups = self._count_components(n_components, wired_connections)

        return {
            "scenario": "Circuit Design Validation",
            "description": "Ensuring all components are properly wired",
            "components": n_components,
            "connections": wired_connections,
            "result": f"Circuit is {'VALID ✓' if circuit_groups == 1 else 'INVALID ✗'} ({circuit_groups} group{'s' if circuit_groups != 1 else ''})",
            "use_case": "PCB Design, Electrical Engineering, Hardware Testing"
        }


def main():
    solver = ConnectedComponentsRealWorld()
    applications = [
        solver.social_network_communities(),
        solver.network_infrastructure_connectivity(),
        solver.image_blob_detection(),
        solver.game_terrain_connectivity(),
        solver.database_deduplication(),
        solver.user_clustering_recommendation(),
        solver.dependency_analysis(),
        solver.circuit_validation(),
    ]

    print("\n" + "="*80)
    print(" CONNECTED COMPONENTS: 8 REAL-WORLD APPLICATIONS ".center(80))
    print("="*80 + "\n")

    for i, app in enumerate(applications, 1):
        print(f"[{i}] {app['scenario'].upper()}")
        print(f"    Description: {app['description']}")
        print(f"    Use Case: {app['use_case']}")
        print(f"    Result: {app['result']}")
        print()

    print("="*80)
    print("Key Insight: All use the same graph algorithm to solve different problems!")
    print("="*80 + "\n")


if __name__ == "__main__":
    main()

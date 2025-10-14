class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def create_cycle(self, pos):
        """Create a cycle at index pos (0-based). pos = -1 means no cycle."""
        if pos == -1:
            return
        cycle_start = None
        current = self.head
        index = 0
        prev = None
        while current:
            if index == pos:
                cycle_start = current
            prev = current
            current = current.next
            index += 1
        if prev:
            prev.next = cycle_start

    def print_list(self, limit=20):
        """Print limited nodes to avoid infinite loop if there's a cycle."""
        current = self.head
        count = 0
        while current and count < limit:
            print(current.data, end=" -> ")
            current = current.next
            count += 1
        print("..." if current else "None")


# time comnp: o(n)
# space comp: o(n)
class SolutionSet:
    def hasCycle(self, head: Node) -> bool:
        visited = set()
        current = head

        while current:
            if current in visited:
                return True  # cycle detected
            visited.add(current)
            current = current.next

        return False





'''
# using floyads' detection algo for o(1) space complexity
class SolutionFloyd:
    def hasCycle(self, head: Node) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True  # pointers met → cycle exists
        return False

'''

def main():
    ll = LinkedList()
    for value in [3, 2, 0, -4]:
        ll.append(value)

    ll.create_cycle(1)  # cycle at index 1 (node with value 2)
    print("Linked List (limited print):")
    ll.print_list()

    print("\nUsing Hash Set Method:")
    print(SolutionSet().hasCycle(ll.head))  # True

    # print("\nUsing Floyd’s Algorithm:")
    # print(SolutionFloyd().hasCycle(ll.head))  # True


if __name__ == "__main__":
    main()

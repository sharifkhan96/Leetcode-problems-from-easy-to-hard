class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

class SolutionDummy:
    def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
        dummy = Node()          # Dummy head to simplify handling head logic
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            x = l1.value if l1 else 0
            y = l2.value if l2 else 0

            total = x + y + carry
            carry = total // 10
            digit = total % 10

            current.next = Node(digit)
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next  # Return actual result list head (skipping dummy)

def printList(node: Node):
    while node:
        print(node.value, end=" -> " if node.next else "")
        node = node.next
    print()



# class Node:
#     def __init__(self, value=0, next=None):
#         self.value = value
#         self.next = next

# class SolutionSimple:
#     def addTwoNumbers(self, l1: Node, l2: Node) -> Node:
#         carry = 0
#         head = None    # Will hold the head of the result list
#         current = None # Will be used to attach further nodes

#         while l1 or l2 or carry:
#             x = l1.value if l1 else 0
#             y = l2.value if l2 else 0
#             total = x + y + carry

#             carry = total // 10
#             digit = total % 10

#             new_node = Node(digit)

#             if head is None:
#                 head = new_node      # First node becomes the head
#                 current = head       # current points to the head
#             else:
#                 current.next = new_node
#                 current = current.next

#             if l1:
#                 l1 = l1.next
#             if l2:
#                 l2 = l2.next

#         return head

# def printList(node: Node):
#     while node:
#         print(node.value, end=" -> " if node.next else "")
#         node = node.next
#     print()
    

def main():
    # Construct two linked lists:
    # l1 = 2 -> 4 -> 3 (represents 342)
    # l2 = 5 -> 6 -> 4 (represents 465)

    l1 = Node(2, Node(4, Node(3)))
    l2 = Node(5, Node(6, Node(4)))

    solver = SolutionDummy()
    result = solver.addTwoNumbers(l1, l2)

    # Should print: 7 -> 0 -> 8 (342 + 465 = 807)
    print("Result:")
    printList(result)

if __name__ == "__main__":
    main()

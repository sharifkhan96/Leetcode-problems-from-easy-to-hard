

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


    def printLinkedList(self):
        current = self.head
        while current:
            print(current.data, end = " -> ")
            current = current.next
        print(None)


    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return 
        
        # finding middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse the 2nd half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge both halves/lists
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        

# O(N) & O(1) for tiime & space complexiities

class main():
    # Create a new linked list
        linked_list1 = LinkedList()

    # Append data to the linked list
        linked_list1.append(1)
        linked_list1.append(2)
        linked_list1.append(3)
        linked_list1.append(4)
        linked_list1.append(5)


    # Print the linked list
        linked_list1.printLinkedList()

        linked_list1.reorderList(linked_list1.head)

        linked_list1.printLinkedList()



if __name__ == "__main__":
    main()

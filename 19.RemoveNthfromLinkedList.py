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

    def removeNthNodefromLinkedList(self, target):
        dummy = Node(0)
        dummy.next = self.head
        fast = dummy
        slow = dummy

        for _ in range(target + 1):
            if fast:
                fast = fast.next

        while fast:
            fast = fast.next
            slow = slow.next

        if slow.next:
            slow.next = slow.next.next

        self.head = dummy.next


        



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

        target = 2#int(input("enter nth node to remove from the end of the linkedlist: "))
        linked_list1.removeNthNodefromLinkedList(target)

        linked_list1.printLinkedList()



if __name__ == "__main__":
    main()
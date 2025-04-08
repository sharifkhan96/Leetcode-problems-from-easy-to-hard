
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

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print(None)


def main():
    # Create a new linked list
        linked_list = LinkedList()

    # Append data to the linked list
        linked_list.append(10)
        linked_list.append(20)
        linked_list.append(30)

    # Print the linked list
        linked_list.print_list()



if __name__ == "__main__":
    main()
# iterative solution


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
    


    def swapPairs(self):
        if not self.head or not self.head.next:
            return self.head
        
        # solutioon with dummy node

        dummy = Node(0)
        dummy.next = self.head
        prev = dummy

        while prev.next and prev.next.next:
            # finding first & second
            first = prev.next
            second = first.next

            # swapping
            prev.next = second
            first.next = second.next
            second.next = first

            # movinng to the next pair
            prev = first


        self.head = dummy.next


        # solutioon without dummy node

        # # Swap first pair manually
        # first = self.head
        # second = first.next
        # self.head = second  # Update head to second

        # first.next = second.next
        # second.next = first

        # prev = first  # Last node of the swapped pair

        # # Now loop through the rest
        # while prev.next and prev.next.next:
        #     first = prev.next
        #     second = first.next

        #     first.next = second.next
        #     second.next = first
        #     prev.next = second

        #     prev = first  # Move to next pair


# complexities:
#   time: O(n)
#   space:  O(1)

def main():
    # Create a new linked list
        linked_list1 = LinkedList()

    # Append data to the linked list
        linked_list1.append(10)
        linked_list1.append(20)
        linked_list1.append(30)
        linked_list1.append(40)
        linked_list1.append(50)

    # Print the linked list
        linked_list1.print_list()

        linked_list1.swapPairs()

        linked_list1.print_list()




if __name__ == "__main__":
    main()
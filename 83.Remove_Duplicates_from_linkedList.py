class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
    

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        new_node = ListNode(val)
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
            print(current.val, end=" -> ")
            current = current.next
        print(None)


def main():
    # Create a new linked list
    linked_list1 = LinkedList()

    # Append data to the linked list
    linked_list1.append(1)
    linked_list1.append(1)
    linked_list1.append(2)
    linked_list1.append(3)
    linked_list1.append(3)

    print("Original List:")
    linked_list1.print_list()

    # Remove duplicates
    obj = Solution()
    linked_list1.head = obj.deleteDuplicates(linked_list1.head)

    print("After Removing Duplicates:")
    linked_list1.print_list()


if __name__ == "__main__":
    main()

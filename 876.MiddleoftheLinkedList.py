from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer = slow_pointer = head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer


def main():
    # Creating a linked list manually
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7, ListNode(8, ListNode(9)))))))))
    obj = Solution()
    middle = obj.middleNode(head)
    print("Middle node value:", middle.val)  # Output the value of the middle node    
    


if __name__ == "__main__":
    main()





""" dynamic linkedlist method 

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast_pointer = head
        slow_pointer = head
        while fast_pointer is not None and fast_pointer.next is not None:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer

def create_linked_list(values: List[int]) -> Optional[ListNode]:
    #Helper function to create a linked list from a list of values
    if not values:
        return None  # Return None if the input list is empty
    
    head = ListNode(values[0])  # Create the head node
    current = head  # Pointer to build the linked list
    
    for value in values[1:]:  # Iterate through the remaining values
        current.next = ListNode(value)
        current = current.next
    
    return head

def print_linked_list(head: Optional[ListNode]) -> None:
    #Helper function to print a linked list.
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")

def main():
    # Input list of values
    values = [1, 2, 3, 4, 5]
    
    # Create linked list from the input values
    head = create_linked_list(values)
    
    # Print the created linked list
    print("Linked list:")
    print_linked_list(head)
    
    # Find the middle node
    obj = Solution()
    middle = obj.middleNode(head)
    
    # Print the middle node value
    print("Middle node value:", middle.val)

if __name__ == "__main__":
    main()


"""
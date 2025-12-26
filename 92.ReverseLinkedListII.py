from typing import Optional

    # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    # time comp: o(n)
    # space com: O(1)
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        # step 1: going till left value
        dummy_head = ListNode(-1, head)
        left_prev, current_node = dummy_head, head
        for i in range(left - 1):
            left_prev = current_node
            current_node = current_node.next

        # step 2 : traversing and reversingggg
        prev = None
        for i in range(right - left + 1):
            next_pointer = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = next_pointer

        # step 3 : cleanup and making approrpriate connections
        left_prev.next.next = current_node
        left_prev.next = prev
        return dummy_head.next

    
    def create_linked_list(self, values: list[int]) -> Optional[ListNode]:
    #Helper function to create a linked list from a list of values
        if not values:
            return None  # Return None if the input list is empty
        
        head = ListNode(values[0])  # Create the head node
        current = head  # Pointer to build the linked list
        
        for value in values[1:]:  # Iterate through the remaining values
            current.next = ListNode(value)
            current = current.next
        
        return head

    def print_linked_list(self, head: Optional[ListNode]) -> None:
        #Helper function to print a linked list.
        current = head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")
        

def main():
    # Creating a linked list manually
    values = [1, 2, 3, 4, 5]

    obj = Solution()
    head = obj.create_linked_list(values)
    # Print the created linked list
    print("Linked list:")
    print(obj.print_linked_list(head))

    reversed = obj.reverseBetween(head, 2, 4)
    print(obj.print_linked_list(reversed))


if __name__ == "__main__":
    main()
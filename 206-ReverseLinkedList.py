from typing import Optional

    # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    
    # time comp: o(n)
    # space com: O(1)
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

            # recursive solution
            # base case:
            if head is None or head.next is None:
                return head
            # step one: reversign the rest of the list
            new_head = self.reverseList(head.next)

            # step two: fixing the current cnode
            head.next.next = head
            head.next = None

            return new_head
        # time & spce complexities: O(N)            


            '''
            current = head
            if not current:
                return
            previous = None
            while current:
                next = current.next
                current.next = previous
                previous = current
                current = next
                
            head = previous
            return head
            '''

    
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

    reversed = obj.reverseList(head)
    print(obj.print_linked_list(reversed))


if __name__ == "__main__":
    main()
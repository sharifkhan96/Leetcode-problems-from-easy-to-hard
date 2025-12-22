from typing import Optional

    # Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next          


class Solution:
    def removeElements(self, head: Optional[ListNode], value: int) -> Optional[ListNode]:
        
        '''
        # recursive solution
        # timem & space comp;: O(N), O(N)
        # base case:
        if head is None:
            return head
        
        head.next = self.removeElements(head.next, value)

        if head.val == value:
            return head.next
        else:
            return head
        '''

        # iterative solutioin
        # time & space complexities: O(N), O(1)
        dummy_head = ListNode(-1)
        dummy_head.next = head
        current_node = dummy_head

        while current_node.next != None:
            if current_node.next.val == value:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
        
        return head #dummy_head.next


    


    
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
    val = 3

    obj = Solution()
    head = obj.create_linked_list(values)
    # Print the created linked list
    print("Linked list:")
    print(obj.print_linked_list(head))

    reversed = obj.removeElements(head, val)
    print(obj.print_linked_list(reversed))


if __name__ == "__main__":
    main()
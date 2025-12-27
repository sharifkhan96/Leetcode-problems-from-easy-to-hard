from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True

        # Step 1: find the middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt

        # Step 3: compare halves
        left = head
        right = prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True


    
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
    values = [1, 2, 1, 2]

    obj = Solution()
    head = obj.create_linked_list(values)

    print("Linked list:")
    obj.print_linked_list(head)

    result = obj.isPalindrome(head)
    print("Is Palindrome:", result)



if __name__ == "__main__":
    main()
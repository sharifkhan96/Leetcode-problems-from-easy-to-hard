# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Base case
        if not head or not head.next:
            return head

        # Step 1: Split the list into halves
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None  # Break the list

        # Step 2: Recursively sort both halves
        left = self.sortList(head)
        right = self.sortList(mid)

        # Step 3: Merge the two sorted halves
        return self.merge(left, right)

    def merge(self, l1, l2):
        dummy = ListNode(0)
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2  # attach the remainder
        return dummy.next

# time comp: O(n log n)
# space comp: O(1)

# Example usage (main function)
def main():
    # Create linked list: 4 -> 2 -> 1 -> 3
    node4 = ListNode(3)
    node3 = ListNode(1, node4)
    node2 = ListNode(2, node3)
    node1 = ListNode(4, node2)

    solution = Solution()
    sorted_head = solution.sortList(node1)

    # Print sorted linked list
    while sorted_head:
        print(sorted_head.val, end=" -> ")
        sorted_head = sorted_head.next
    print("None")


if __name__ == "__main__":
    main()

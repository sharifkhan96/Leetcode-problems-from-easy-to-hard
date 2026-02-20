from typing import List, Optional
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Push the first node of each list into the heap
        for i, head in enumerate(lists):
            if head:
                heapq.heappush(heap, (head.val, i, head))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)

            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        tail.next = None
        return dummy.next


# ----------------------------
# Helper functions
# ----------------------------

def build_linked_list(arr):
    if not arr:
        return None
    
    dummy = ListNode(0)
    current = dummy
    
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    
    return dummy.next


def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")


# time comp: o(N log k)
# space comp: O(k)

# ----------------------------
# Main 
# ----------------------------

def main():
    input_lists = [[1,4,5],[1,3,4],[2,6]]

    # Convert arrays to linked lists
    linked_lists = [build_linked_list(lst) for lst in input_lists]

    obj = Solution()
    merged_head = obj.mergeKLists(linked_lists)

    print_linked_list(merged_head)


if __name__ == "__main__":
    main()
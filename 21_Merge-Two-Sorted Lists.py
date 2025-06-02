# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



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



class Solution: # this punction is our mainnnnnnnnnnnnnnnnnnn & core logic
    def mergeTwoLists(self, list1, list2): # type: ignore
        if not list1:
            return list2
        if not list2:
            return list1
        

        if list1.data < list2.data:
            head = list1
            list1 = list1.next
        else:
            head = list2
            list2 = list2.next

        current = head

        while list1 and list2:
            if list1.data < list2.data:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        return head




def main():
        # Create a new linked list
        linked_list = LinkedList()

    # Append data to the linked list
        linked_list.append(1)
        linked_list.append(2)
        linked_list.append(4)

    # # Print the linked list
    #     linked_list.print_list()

    # ------------------------------

        linked_list2 = LinkedList()
        
        linked_list2.append(1)
        linked_list2.append(3)
        linked_list2.append(4)

        # linked_list2.print_list()

        obj1 = Solution()
        # Pass head nodes, not full LinkedList objects
        result = obj1.mergeTwoLists(linked_list.head, linked_list2.head)

        # Print merged result
        merged_list = LinkedList()
        merged_list.head = result
        merged_list.print_list()

        
        

if __name__ == "__main__":
    main()
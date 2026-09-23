# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # The resultant list
        head = None
        current = None

        def addToList(node: Optional[ListNode]):
            nonlocal head, current
            if head:
                current.next = node
                current = node
            else:
                head = node
                current = node

            

        while list1 and list2:
            if list1.val <= list2.val:
                addToList(list1)
                list1 = list1.next
            else:
                addToList(list2)
                list2 = list2.next
        
        while list1:
            addToList(list1)
            list1 = list1.next

        while list2:
            addToList(list2)
            list2 = list2.next

        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        list3 = []
        
        while list1:
            list3.append(list1.val)
            list1 = list1.next
            
        while list2:
            list3.append(list2.val)
            list2 = list2.next
        list3 = sorted(list3)
        
        uns = ListNode(None)
        curr_el = uns
        for el in list3:
            curr_el.next = ListNode(el)
            curr_el = curr_el.next
        
        return uns.next

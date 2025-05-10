class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        uns = None
        while head:
            temporary = head.next
            head.next = uns
            uns = head
            head = temporary
        
        return uns

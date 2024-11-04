class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Dummy node to start the result list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0

        # Iterate through both lists
        while l1 or l2 or carry:
            # Get the current values and move to the next nodes
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry

            # Update carry and current node's value
            carry = total // 10
            current.next = ListNode(total % 10)

            # Move to the next elements in the list
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next
        

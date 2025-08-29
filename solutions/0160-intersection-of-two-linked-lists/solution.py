# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        tryA = headA
        lenA = 1
        while tryA.next:
            tryA = tryA.next
            lenA += 1
        lastA = tryA.val

        tryB = headB
        lenB = 1
        while tryB.next:
            tryB = tryB.next
            lenB += 1
        lastB = tryB.val

        if lastA!=lastB:
            return None

        if lenA>lenB:
            while lenA>lenB:
                headA = headA.next
                lenA -= 1
        elif lenA<lenB:
            while lenA<lenB:
                headB = headB.next
                lenB -= 1
        
        no_intersection = True
        while no_intersection:
            if headA == headB != None:
                return headA
            elif headA == headB == None:
                return False
            else:
                headA = headA.next
                headB = headB.next
            



        

        



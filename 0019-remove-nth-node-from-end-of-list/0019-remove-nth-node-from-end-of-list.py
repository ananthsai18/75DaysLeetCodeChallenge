# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow=head
        l=0
        while slow:
            l+=1
            slow=slow.next
        
        k=l-n
        if k == 0:
            return head.next
            
        prev = None
        rn=0
        curr=head
        while curr:
            temp=curr.next
            if rn==k:
                prev.next = temp
                return head
            prev=curr
            curr=curr.next
            rn+=1
        return head

        









        
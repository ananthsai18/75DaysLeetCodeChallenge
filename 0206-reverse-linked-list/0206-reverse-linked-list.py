# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # C=BRute force
        t=head
        curr=head
        stack=[]    
        while curr:
            stack.append(curr.val)
            curr=curr.next
        print(stack)

        curr=head
        
        while curr and stack:
            curr.val=stack.pop()
            
            curr=curr.next
        return t
    

        
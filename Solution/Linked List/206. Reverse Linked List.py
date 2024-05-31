# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head:
        #     return
        # if head.next==None:
            
        #     return head
        # prev=None
        # current=head
        # after=current.next
        # while(current!=None):
        #     current.next=prev
        #     prev=current
        #     if after==None:
        #         break
        #     current=after
        #     after=after.next
        # return current
        if not head:
            return None
        new_head=head
        if head.next: 
            new_head=self.reverseList(head=head.next)
            head.next.next=head
        head.next=None
        return new_head
            

        

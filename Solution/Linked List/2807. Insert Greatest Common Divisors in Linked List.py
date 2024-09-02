# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a,b):
            while b:
                a,b=b,a%b
            return a
        current=head
        while current and current.next:
            result=gcd(current.val,current.next.val)
            new_node=ListNode(result,next=current.next)
            current.next=new_node
            current=new_node.next
        return head

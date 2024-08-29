# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    time:O(n) 遍歷整個串列需要O(n) 每次遍歷把整個數組向左移一個 相當於乘上二的冪次方 再加上當前head的value值
    space:O(1)
    """
    def getDecimalValue(self, head: ListNode) -> int:
        ans=0
        while head!=None:
            ans=ans*2+head.val
            head=head.next
        return ans
       
        

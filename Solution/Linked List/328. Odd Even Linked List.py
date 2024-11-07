# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    note
    head 會指向第一個node 
    所以head.next 為第二個node
    head.next.next 是第三個node 

    time:O(n) 整個list 遍歷一次 
    space:O(1)
    """
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #edge case 當長度為0,1時
        if head is None or head.next is None:
            return head

        #用雙指針分別指向index奇數與偶數位置
        odd=head
        even=head.next
        
        #最後要奇數的next 指向的一個偶數index的位置
        even_head=even 
        while even and even.next: #代表下一個奇偶index都存在
            odd.next=even.next
            odd=odd.next
            
            #若最後一個index是奇數
            if odd.next is None:
                odd.next=even_head
                even.next=None
            #偶數
            else:
                even.next=odd.next
                even=even.next
        odd.next=even_head
        return head

        

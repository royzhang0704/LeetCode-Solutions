# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    time:O(n) 雖然insert delete都是O(1) 但如果插入在最後面 且沒有額外的指針指向最後一個元素 那麼插入需要O(n) 
    space:O(1):無額外創建的空間
    """
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy_node=ListNode(next=head)
        current=dummy_node
        while current.next!=None:
            if current.next.val==val:
                current.next=current.next.next
            else:
                current=current.next
        return dummy_node.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    time:O(n): 遍歷每個節點
    space:O(n) 把nums轉成set 不然每次remove都要O(n)的時間 
    """
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ans=0
        nums=set(nums)
        while head: 
            if head.val in nums:#當前節有點在nums裡面
                nums.discard(head.val)
                while head.next is not None and head.next.val in nums: #找出連續鄰居
                    nums.discard(head.next.val)
                    head=head.next
                ans+=1 #第一個head 在nums 裡面的為同一組 
            head=head.next 
        return ans

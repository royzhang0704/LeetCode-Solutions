# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        所以他不是給我們一整個串列節點 讓我們從head開始 
        我們一般都是從頭開始遍歷 直到遇到下一個節點是我們的目標 我們就把當前目標指向下下一個節點 
        相當於移除目標節點 但是我們現在只有一個node指針指向 要刪除的節點 我們沒辦法透過 上一個節點指向下下個節點
         只能從當節點去操作 又因為刪除的節點不會是最後一個節點 也就是node.next 不會為空 
         所以我們可以變項的把當前要刪出的節點值變成下一個節點的值 並把指針指向下下個節點 
         也變成相當於是 刪除了該節點的下一個節點 

        time:O(1)
        space:O(1)
        """
        node.val=node.next.val
        node.next=node.next.next
        

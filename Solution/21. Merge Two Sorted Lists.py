# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        dummy=ListNode(0) #創一個dummy Node
        current=dummy
        while list1 is not None and list2 is not None: #兩個List都不為空 判斷是哪個Node要插入
            if list1.val<list2.val: #list1的比較小
                current.next=list1 #插入
                list1=list1.next #更新list1當前節點
            else:
                current.next=list2 
                list2=list2.next
            current=current.next #這一行很重要 我沒寫 導致list的長度不會增加 只是一直改變而已 直到有某個list為空 才把另一個list整到放入 
        
        
        #有其中一個為空 把另外一個list直接放入 
        if  list1 is None and list2 is not None:
            current.next=list2
        if list1 is not None and list2 is None:
            current.next=list1

        return dummy.next dummy 第一個為我們創造的Node val=0 從第二個開始才是list1,list2的元素

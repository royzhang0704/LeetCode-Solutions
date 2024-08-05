class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
"""
共有5個功能 
get index上的val 
增加一個node為新的head  
在尾巴新增一個node  
在某個index 前面新增一個node 
刪除某個node index 不固定
"""
class MyLinkedList: 
    def __init__(self):
        self.dummy_head=ListNode() #創建一個虛擬頭節點
        self.size=0 #size default=0  
    def get(self, index: int) -> int:#
        if index<0 or index >=self.size:
            return -1
        head=self.dummy_head.next
        for i in range(index):
            head=head.next
        return head.val
    def addAtHead(self, val: int) -> None:
        self.dummy_head.next=ListNode(val=val,next=self.dummy_head.next)
        self.size+=1

    def addAtTail(self, val: int) -> None:
        if self.dummy_head.next is None:
            self.dummy_head.next=ListNode(val=val,next=None)
        else:
            head=self.dummy_head.next
            while head.next is not None:
                head=head.next
            head.next=ListNode(val=val,next=None)
        self.size+=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index>=0 and  index <=self.size:
            head=self.dummy_head
            for i in range(index):
                head=head.next
            head.next=ListNode(val=val,next=head.next)
            self.size+=1
    def deleteAtIndex(self, index: int) -> None:
        if index>=0 and index <self.size:
            head=self.dummy_head
            for i in range(index):
                head=head.next
            head.next=head.next.next
            self.size-=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

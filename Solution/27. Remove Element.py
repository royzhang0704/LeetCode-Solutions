class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast=0#用來掃整個array
        slow=0#用來紀錄元素不等於value的index 
        while(fast<len(nums)):
            if nums[fast]!=val: 
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow

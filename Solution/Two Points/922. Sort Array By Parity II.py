"""
time:O(n):利用odd與even兩個指針個跑O(n/2)次 共O(n)
space:O(1)沒有額外創建array 
"""
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even=0
        odd=1
        n=len(nums)
        while odd<n and even<n:
            if nums[even]%2==0:
                even+=2
            elif nums[odd]%2==1:
                odd+=2
            else:
                nums[even],nums[odd]=nums[odd],nums[even]
        return nums

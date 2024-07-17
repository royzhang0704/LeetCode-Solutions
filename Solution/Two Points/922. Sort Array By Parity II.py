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
            while even<n and  nums[even]%2==0 :
                even+=2
            while  odd<n and nums[odd]%2!=0:
                odd+=2
            if even<n and odd<n:
                nums[even],nums[odd]=nums[odd],nums[even]
        return nums

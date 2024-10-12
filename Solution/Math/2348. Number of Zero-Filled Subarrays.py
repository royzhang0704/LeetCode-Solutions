class Solution:
    """
    time:O(n) 每個數組只會遍歷一次 
    space:O(1)
    """
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        ans=count=0
        for value in nums:
            if value==0:
                count+=1
                ans+=count
            else:
                count=0
        return ans

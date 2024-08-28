class Solution:
    """
    time:O(N)
    space:O(1)
    """
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current=0
        ans=0
        for i in nums:
            if i ==1:
                current+=1
                ans=max(ans,current)
            else:
                current=0
        return ans

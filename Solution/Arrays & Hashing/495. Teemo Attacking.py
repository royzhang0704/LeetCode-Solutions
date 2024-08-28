class Solution:
    """
    time:O(n)
    space:O(1)
    """
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans=0
        n=len(timeSeries)-1
        for i  in range(n):
            ans+=min(timeSeries[i+1]-timeSeries[i],duration)
        ans+=duration
        return ans
        

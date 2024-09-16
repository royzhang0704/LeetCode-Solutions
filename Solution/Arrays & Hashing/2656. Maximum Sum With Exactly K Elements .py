class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        ans=0
        nums.sort()
        while k:
            n=nums.pop()
            ans+=n
            nums.append(n+1)
            k-=1
        return ans

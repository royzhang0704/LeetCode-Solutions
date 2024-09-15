class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_=max(nums)
        min_=min(nums)
        ans=0
        for i in nums:
            if i != max_ and i!=min_:
                ans+=1
        return ans

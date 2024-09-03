class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """
        time:O(n)
        space:O(1)
        """
        left=0
        right=len(nums)-1
        while left<right:
            if nums[left]%2==1 and nums[right]%2==0:
                nums[left],nums[right]=nums[right],nums[left]
            if nums[left]%2==0:
                left+=1
            if nums[right]%2==1:
                right-=1
        return nums

class Solution:
    """
    二分搜:O(logn) 適用於已經sort好的array
    """
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(right+left)//2 #防止overflow寫法 mid=(left+(right-left))/2
            if nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
            else:
                return mid
        return left

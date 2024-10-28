def lower_bound(nums,target):
    left,right=0,len(nums)
    while left<right:
        mid=left+((right-left)>>1)
        if nums[mid]<target:
            left=mid+1
        else:
            right=mid
    return left
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start_index=lower_bound(nums,target)
        if start_index==len(nums) or nums[start_index]!= target:
            return [-1,-1]
        end_index=lower_bound(nums,target+1)-1
        return [start_index,end_index]

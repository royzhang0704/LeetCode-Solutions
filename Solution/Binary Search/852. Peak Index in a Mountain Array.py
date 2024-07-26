class Solution:
    """
    time:O(logn)
    space:O(1)
    """
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left=0
        right=len(arr)-1
        while left<right:
            mid=(right+left)//2
            if arr[mid]>arr[mid+1]: #mid 本身就是峰值或其左侧有一个峰值
                right=mid
            else:# mid 右侧有一个峰值
                left=mid+1
        return left 

class Solution:
    """
    time:O(n)
    space:O(1)
    """
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left=0
        right=x//2
        while left<=right:
            mid=(right+left)//2
            if mid**2==x:
                return mid
            elif mid**2<x:
                left=mid+1
            elif mid**2>x:
                right=mid-1
        return right

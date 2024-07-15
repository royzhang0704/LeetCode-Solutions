"""
time complexity:O(n) 指針移動次數共n次 每次計算出當下面積與比較當前最大面積只需O(1)
space complexity:O(1): 只有用到常數變量 無額外的array空間
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans=0
        left=0
        right=len(height)-1
        while left < right:
            area=(right-left)*min(height[left],height[right])
            ans=max(ans,area)
            if height[left]<height[right]:
                left+=1
            else: #若兩邊相等 左右point 哪邊動都可以
                right-=1
        return ans

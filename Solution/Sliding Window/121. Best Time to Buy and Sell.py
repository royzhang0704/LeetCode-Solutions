"""
先令第一天買入 若找到當比當前買入的點還低 把它設為買入 在與後面的賣出 相減找出最大值
time:O(n):array只會掃一次 
space:O(1): 只用到一些常數變量
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        buy=prices[0]
        for i in prices:
            if i<buy:
                buy=i
            ans=max(ans,(i-buy))
        return ans

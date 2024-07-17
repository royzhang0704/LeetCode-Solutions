"""
想法
題目都是正整數 不能排序 要計算出最短子陣列i.e.連續的用貪心會找不到最佳解
若從index=0 到當前index=right的總和都大於代表子陣列長度可以在短
time:O(n):雖然有一個for loop 加上一個while loop 
        但while loop移動指針次數最多只會到n長度
        array每個元素都透過for loop枚舉一次共O(n)
        加上while loop 指針最多移動n次=O(n),
        total=O(n)+O(n)=O(2n)=O(n)
space:O(1) 只用到幾個常數變量(left、current_sum、n、ans 和 right）
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=0
        current_sum=0
        n=len(nums)
        ans=n+1 #方便用來紀錄最小值 相當於代表infinit 
        for right,x in enumerate(nums): #當前right為子array的右端點
            current_sum+=x
            while current_sum-nums[left]>=target:
                current_sum-=nums[left]
                left+=1
            if current_sum>=target:#代表當前從left到right指針的長度總>=target  否則沒必要更新ans值
                ans=min(ans,right-left+1) 
        return ans if ans<=n else 0 #若ans 不超過array size

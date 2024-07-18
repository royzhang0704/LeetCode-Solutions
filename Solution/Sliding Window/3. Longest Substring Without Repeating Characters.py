"""
time:O(n) 指針只會跑到n次 並且每次都去查找當前元素是否在dictionary裡面 {elemant:index},若當前元素有出現過且出現在當前left指標的後面 把left指標更新到該index+1位置 每回更新ans值
space:O(n)用hash_table來存放每個元素的index位置 worst case 每個元素都不一樣 至多需要O(len(s))的空間
left-right是否要+1
當只有一個元素時 另index=5 left=right=5 ans=5-5+1 長度為1 才符合
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = {}
        ans = 0
        left = 0
        
        for right, char in enumerate(s):
            if char in table and table[char] >= left:
                left = table[char] + 1
            table[char] = right
            ans = max(ans, right - left + 1)
        
        return ans

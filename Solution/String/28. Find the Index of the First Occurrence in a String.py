class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        """
        time:O((m-n)*n)=O(m*n) m為haystack的長度 while迴圈的次數會為len(haystack)-len(needle) i.e. m-n
        space:O(1)
        """
        if len(needle) > len(haystack): #needle比haystack 則不存在Case
            return -1
        
        left = 0
        while left +len(needle) <=len(haystack):  # 確保從 haystack 剩餘部分能容納 needle
            if haystack[left:left + len(needle)] == needle: 
                return left
            left += 1
        return -1

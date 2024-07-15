"""
透過移除一個字元 是否能達變成迴文
aba -> 本身就是迴文
abca -> 移除c 
想法:return 移除不匹配的元素　看是否能形成回文
time:O(n)　當出現有不匹配的字串需要三次Ｏ(n)的雙指針判斷(O(n)+O(n-1)+O(n-1))=O(3n-2)=O(n) 　就算原字串為迴文也需要跑一次Ｏ（ｎ）雙指針 
space:O(1) 無額外創建ａｒｒａｙ
"""
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isvalid(s,start,end):
            left=start
            right=end
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        left=0
        right=len(s)-1
        while left<right:
            if s[left]!=s[right]:
                return isvalid(s,left+1,right) or isvalid(s,left,right-1)
            else:
                left+=1
                right-=1
        return True

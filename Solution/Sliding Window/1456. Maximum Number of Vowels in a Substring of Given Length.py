class Solution:
    """
    窗口需要兩個指針維護 頭跟尾
    窗口移動時 左指針向右移動之前先判斷如果當前left index位置剛好是母音 要把res-1
    右指針移動時判斷新的右指針的元素是否是母音 如果是做res+1 之後再去更新res值
    直到left>len(s)-k 位置
    abciiidef
    left 最多走到len(s)-k 
    窗口向前一步

    leetcode 
      ans=2
    """
    def maxVowels(self, s: str, k: int) -> int:
        target="aeiou"
        left,right=0,k-1
        n=len(s)
        current=0
        ans=0
        for i in range(k):
            if s[i] in target:
                current+=1
        ans=max(ans,current)
        while left!=n-k and right!=n-1:
            if s[left] in target:
                current-=1
            left+=1
            right+=1
            if s[right] in target:
                current+=1
            ans=max(ans,current)
        return ans

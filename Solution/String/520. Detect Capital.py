class Solution:
    """
    time:O(n) 遍歷一次數組 算出大寫次數 
    若大寫次數跟字串長度相同代表全大寫
    若為0全寫寫也可
    若count=1 則大寫的位置一定要是開頭
    space:O(1)
    """
    def detectCapitalUse(self, word: str) -> bool:
        count=sum(i.isupper() for i in word)
        return count==0 or count==len(word) or count==1 and word[0].isupper()

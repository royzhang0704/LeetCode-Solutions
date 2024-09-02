class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        """
        time:O(n) 分別處理兩個字串 total O(m)+O(k) len(s)=m len(t)=k
        space:O(n) 創建一個result 來裝結果
        """
        def deal (string):
            result=[]
            for i in range(len(string)):
                if string[i]!="#":
                    result.append(string[i])
                elif string[i]=="#" and len(result):
                    result.pop()
            return result

        return deal(s)==deal(t)

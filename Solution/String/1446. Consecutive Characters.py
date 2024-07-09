class Solution:
    def maxPower(self, s: str) -> int:
        result=1
        count=1
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                count+=1
            else:
                result=max(count,result)
                count=1
        result=max(count,result)
        return result

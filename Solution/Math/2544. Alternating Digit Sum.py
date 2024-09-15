class Solution:
    def alternateDigitSum(self, n: int) -> int:
        if n<10:
            return n
        ans,sign=0,1
        while n:
            ans+=n%10*sign
            sign=-sign
            n//=10
        return ans*-sign

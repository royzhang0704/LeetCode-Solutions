class Solution:
    def alternateDigitSum(self, n: int) -> int:
        ans,sign=0,1
        while n:
            ans+=n%10*sign
            sign=-sign
            n//=10
        return ans

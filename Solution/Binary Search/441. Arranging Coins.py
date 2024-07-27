class Solution:
    def arrangeCoins(self, n: int) -> int:
        k=1
        while n>=((1+k)*k)/2:
            k+=1
        return k-1
        


"""
1+2+3=[(1+3)*3]/2=6
"""

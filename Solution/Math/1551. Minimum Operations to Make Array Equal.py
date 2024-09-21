class Solution:
    def minOperations(self, n: int) -> int:
        ans=0
        last_num=2*n-1
        total=(1+last_num)*n//2
        target=total//n
        start=1
        while start<target:
            ans+=target-start
            start+=2
        return ans

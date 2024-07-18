class Solution:
    """
    def missingNumber(self, nums: List[int]) -> int:
        table={}
        for i in nums:
            table[i]=table.get(i,0)+1
        for i in range(len(nums)+1):
            if i not in table:
                return i
    time:O(n)
    space:O(n)
    不夠好
    """

    """
    已知長度為n的array 其區間為[0,n] 總和為0+1+2+....+n=[(0+n)*(n+1)]/2
    把總和扣掉當前array的sum差值就是missing number
    time:O(n):計算出total總和
    space:O(1):無用到無外的空間
    """
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=n*(n+1)//2
        # total=sum([i for i in range(n)])
        return total-(sum(nums))

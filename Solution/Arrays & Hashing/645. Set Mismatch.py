class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        table={}
        for i in nums:
            table[i]=table.get(i,0)+1
        for i in range(1,len(nums)+1):
            if i not in table:
                miss=i
            elif table[i]==2:
                dup=i
        return [dup,miss]

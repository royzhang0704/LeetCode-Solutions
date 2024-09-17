class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        table=set()
        for i in nums:
            if i not in table:
                table.add(i)
            else:
                return i

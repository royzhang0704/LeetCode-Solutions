class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        ans=set(nums)
        for i in nums:
            k=self.reverse_num(i)
            if k not in ans:
                ans.add(k)
        return len(ans)
    def reverse_num(self,num):
        return int(str(num)[::-1])

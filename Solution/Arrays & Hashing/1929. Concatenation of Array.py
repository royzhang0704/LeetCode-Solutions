class Solution:
    """
    time:O(n)
    space:O(2n)=O(n)
    """
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result=[0]*(len(nums)*2)
        for i in range(len(nums)):
            result[i],result[len(nums)+i]=nums[i],nums[i]
        return result

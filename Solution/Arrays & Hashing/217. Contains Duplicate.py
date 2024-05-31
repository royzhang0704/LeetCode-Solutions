class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result=set()
        for i in range(len(nums)):
            if nums[i] not in result:
                result.add(nums[i])
            else:
                return True
        return False

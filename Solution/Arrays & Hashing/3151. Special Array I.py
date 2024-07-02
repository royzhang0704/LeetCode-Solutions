class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        is_even_index_even=nums[0]%2==0
        
        for i in range(len(nums)):
            if i%2==0:
                if (nums[i]%2==0)!=is_even_index_even:
                    return False
            else:
                if (nums[i]%2==0)==is_even_index_even:
                    return False
        return True

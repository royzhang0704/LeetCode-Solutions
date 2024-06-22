class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        result = 0
        
        while left < right:
            if nums[left] + nums[right] < target:
                # 當 nums[left] + nums[right] < target 時，從 left 到 right-1 都可以形成有效數對
                result += right - left
                left += 1
            else:
                right -= 1
        
        return result

"""
time complexity: O(n log n)
排序數組需要 O(n log n) 時間
雙指針掃描需要 O(n) 時間
總時間複雜度 = O(n log n)

space complexity: O(1)
除了排序所需的額外空間，雙指針掃描只需要常數空間
總空間複雜度 = O(1)
"""

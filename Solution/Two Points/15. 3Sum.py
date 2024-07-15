"""
time:O(n^2)
space:O(n)
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for left in range(len(nums)-2):
            if left>0 and nums[left-1]==nums[left]:
                continue
            mid=left+1
            right=len(nums)-1
            while mid < right:
                total=nums[left]+nums[mid]+nums[right]
                if total==0:
                    result.append([nums[left],nums[mid],nums[right]])
                    while mid<right and nums[mid]==nums[mid+1]:
                        mid+=1
                    while mid<right and nums[right]==nums[right-1]:
                        right-=1
                    mid+=1
                    right-=1
                elif total>0:
                    right-=1
                else:
                    mid+=1
        return result
                    

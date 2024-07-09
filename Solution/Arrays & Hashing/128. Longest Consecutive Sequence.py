#hash set
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        #轉成hashset 不包含相同元素
        nums_set=set(nums)
        result=1
        for i in nums_set:
            if i-1 in nums_set:
                continue
            current_number=i
            current_length=1
            while current_number+1 in nums_set:
                current_number+=1
                current_length+=1
            result=max(result,current_length)
        return result

"""
time complexity:O(n) 遍歷每個element 在table做查找只需要O(1)
space  complexity:O(n):把N個元素存進table 
"""

#排序暴力法
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        nums.sort()
        count=1
        result=1
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                count+=1
            elif nums[i]!=nums[i+1]:
                result=max(count,result)
                count=1
        result=max(count,result)
        
        return result




"""
time complexity:  O(nlogn)
                那如果這題用排序去解題的話 排序需要先O(nlogn)的時間
                之後每個元素去比較後面一個元素檢查是否為遞增 每個元素最多被比較兩次 共需O(2n)=O(n)
                total=O(nlogn)+O(n)=O(nlog)
space  complexity:O(1):只有一個result 常數變量存ans
"""

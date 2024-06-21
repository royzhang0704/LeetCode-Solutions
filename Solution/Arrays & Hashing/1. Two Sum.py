"""
暴力法
time complexity:O(n^2) 
第一個元素比對n-1次 
第二個元素比對n-2 
total cost =(n-1)+(n-2)+(n-3)+......+1
=(1+(n-1)*n-1)/2 =O(n^2)
space complexity:O(1)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result=[]
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    result.append(i)
                    result.append(j)
        return result
                    


"""
哈希表法
time complexity: O(n) 
每個元素都檢查其 diff 是否存在
最終遍歷整個 array 可以得到唯一解
space complexity: O(n) 
最多需要存儲 n 個元素在字典中
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}  # key: target - num, value: index of array
        for index, value in enumerate(nums):  # 用 enumerate 來得到 array 的 index 和對應的 value
            if value not in diff:  # 若當前 diff 字典裡沒有當前的 key 值
                diff[target - value] = index  # 把該元素與 target 的 diff 當作字典的 key，把對應的 index 當作字典的 value
            else:
                return [diff[value], index]  # 若當前的 element 已在字典中，則返回相應的 index




"""
雙指針法
time complexity: O(n) 只需遍歷整個 array 一次
space complexity: O(1) 沒有額外的儲存空間
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = sorted((num, index) for index, num in enumerate(nums))  # 生成 (num, index) 的 tuple 並排序
        left, right = 0, len(nums) - 1
        
        while left < right:
            current_sum = num_index[left][0] + num_index[right][0]
            if current_sum == target:
                return [num_index[left][1], num_index[right][1]]
            elif current_sum < target:
                left += 1
            else:
                right -= 1







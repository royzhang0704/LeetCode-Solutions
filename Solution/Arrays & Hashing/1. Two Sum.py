"""
暴力法
time complexity:O(n^2) 第一個元素比對n-1次 第二個元素比對n-2 total cost =(n-1)+(n-2)+(n-3)+......+1=(1+(n-1)*n-1)/2 =O(n^2)
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
hash table 
time complexitu:O(n) 每個元素都去檢查他的diff 是否存在 最後遍歷整個array 可以得到唯一解
space complexity:O(n) 有n個元素則dictionary 共要最多要push len(nums)個進去  len(nums)=n
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     diff={}     #key:target-num  value:index of array
     for index,value in enumerate(nums):     #用enumerate來得到array的index 跟對應的value
        if diff.get(value,None)==None:     #若當前diff 字典裡沒有當前的key值
            diff[target-value]=index     #把該元素的與target的diff當作字典的key 把對應的index 當作hash table 的value
        else:
            return [index,diff[value]]    #若當前的element 已經在hash table 代表先前有某個元素的與當前元素相加會相等 且字典value為該元素的index 
                    #return 的第一個index 為當前元素的index diff[value] 為另個元素與當前元素相加為target的index



"""
two pointer
time complexity:O(n) 只會遍歷整個array一次
space complexity:O(1) 沒有額外的儲存空間
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index=list(zip(nums,range(len(nums))))    #把每個元素都跟他的index 做zip  tuple 的format 為(num,index)
        num_index.sort()#sort 會根據tuple 的第一個元素去做排序

        #num_index是一個list 而每個list 的element都是一個tutle 

        left=0
        right=len(nums)-1

        while left <right:
            current_sum=num_index[left][0]+num_index[right][0] #tuple 的index 0 是num , index 1 是index 
            if current_sum==target:
                return [num_index[left][1],num_index[right][1]]
            elif current_sum<target:
                left+=1
            else:
                right-=1








class Solution:
    """
    分別討論case
    case 1:當數組都沒有負數 
        最大值一定是前三大的數字
    
    case2:當數組出現一個負數
        一定也還是前三大數字相乘為最大樹
    
    case3:有兩個負數
    有能可是最小的兩個負數相乘為一個很大的正數 再去跟正數的最大數相乘
    
    case4:三個負數
    還是會為最大3數相乘為ans

    """
    """
    time:O(nlogn) 排序
    space:O(1)
    """
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[0]*nums[1]*nums[-1])

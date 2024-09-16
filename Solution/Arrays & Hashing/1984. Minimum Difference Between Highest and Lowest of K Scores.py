class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:

        """
        time:O(nlogn) 對數組排序需O(nlogn) 之後在遍歷len(nums)-k+1次後 找出k位學生中差的最小值需要O(n)
        space:O(l) 對原術組進行排序 用result 紀錄當前最小值
        
        """
        #edge case 只有一位的話自己是最大值同時也是最小值 diff=0
        if k==1:
            return 0
        result=float('inf')
        nums.sort() #先對數組進行排序 結果才可預期 可以知道區間的最大最小值
        for i in range(len(nums)-k+1):
            result=min(result,nums[i+k-1]-nums[i]) #index i+k+1為該區間的最到值 i為乾區間的最小值

        return result

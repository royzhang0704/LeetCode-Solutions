class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        """
        time=O(n) 遍歷數組每個元素 去計算它的出現頻率跟是為第一次出現 兩次字典查詢都是O(1)
            之後會再遍歷一次數組檢查dreege數是否為max_degree 如果是去計算他們數組區間位置 取最小
            total=O(n)+O(n)=O(n)
        space:O(n):創建了三個hash_table 分別記錄元素的出現次數 起始位置跟最後一次出現的位置
            假設每個元素都是一樣的那麼count,left,right只會有一個值,若都不一樣三個table都是O(n)
            total=O(3n)=O(n)
        """
        max_degree=0
        count={}
        left={}
        right={}
        result=len(nums)
        for index,value in enumerate(nums):
            count[value]=count.get(value,0)+1
            if value not in left:
                left[value]=index
            right[value]=index
            max_degree=max(max_degree,count[value])
        for i in nums:
            if count[i]==max_degree:
                result=min(result,right[i]-left[i]+1)
        return result

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """
        time:(nlogn):處理數字和需要O(nlogn)的時間,之後遍歷一次數組 每次查詢需要O(1)時間共n次 total=O(nlogn)+O(n)=O(nlogn)
        space:O(n):若每個數字和都不一樣需要創建n個不同的num_sum 



        edge case:
            若每個數字的位數和都一樣? 怎麼維護最大值？
            每次成功配對時 去維護當前值是否比當前table value的值還要大 若還要大需要更新
            
        """
        def num_sum(n):
            result=0
            while n:
                result+=n%10
                n//=10
            return result
        table={}
        ans=-1
        for i in nums:
            if num_sum(i) in table:
                ans=max(ans,table[num_sum(i)]+i)
                table[num_sum(i)]=max(table[num_sum(i)],i)
            else:    
                table[num_sum(i)]=i
        return ans
            

class Solution:
    """
    time:O(n):滑動視窗 遍歷整array一次
    space:O(1):最多只有26個組個數 i.e.O(26)=O(1)
    """
    
    def characterReplacement(self, s: str, k: int) -> int:
        counter=Counter() #創建一個hash table {element:count}
        left,right=0,0
        ans=0
        max_freq=0
        while right<len(s): #當前元素還沒的最後一個
            counter[s[right]]+=1
            max_freq=max(max_freq,counter[s[right]])
            while (right-left+1)-max_freq>k: #頻率出現次數較少的元素大於可以修改次數 代表無法行程連續子串列 
                counter[s[left]]-=1 #把數組左左邊的元素從hash扣除一之後把left 指針移動一格
                left+=1
            ans=max(ans,right-left+1) #若找到符合條件[left,right]此區間得技術符合<=k update 當前ans
            right+=1 #把當前right指針 直到移動到array last position
        return ans 

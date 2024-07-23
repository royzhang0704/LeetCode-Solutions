class Solution:
    """
    time:O(n) 
    創建count需要O(n)把整個array遍歷一次 之後count每個key丟到桶子需要O(n) 這個list需要len(max(count.values()))<=O(n) 之後再對每個list 排序需要O(nlogn) append到result也需要O(n) 共O(n)+O(n)+O(nlogn)+O(n)=O(nlogn)
    space:O(n)
    創建countO(n) 創建resultO(n) 共O(n)
    """
    def frequencySort(self, nums: List[int]) -> List[int]:
        count=Counter(nums)
        max_length=max(count.values())
        result=[]
        buket=[[] for _ in range((max_length)+1)] #頻率最高得桶子size+1
        for num,cou in count.items():
            buket[cou].append(num) #把element丟到桶子 其中index為頻率
        for i in range(len(buket)): #對list of list 進行sort
            if buket[i]:
                buket[i].sort(reverse=True) #decreasing 
                for num in buket[i]:
                    result.extend([num]*i) #當前每隔list 元素都為一 被轉成dictionary 需要重複push push的次數為當前index 也就是出現的頻率
        return result
    """
        count={1:2,2:3,3:1}
    ==>      [[] [3] [2,1] []]
frequency     0  1. 2 3
    result=[3,2,2,1,1]
    """
                    

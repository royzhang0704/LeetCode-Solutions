class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}# {element:frequency}
        frequency=[[] for i in range(len(nums)+1)] #創建一個burket 
        result=[] 
        for num in nums:
                count[num]=count.get(num,0)+1
        for num,fre in count.items():
            frequency[fre].append(num)

        for i in range(len(nums),0,-1):
            for element in frequency[i]:
                result.append(element)
                if len(result)==k:
                    return result
        return result
        

"""
Time complexity:時間為O(n) 先創建一個字典把每個元素都計算出他的頻率需要O(n)
                每個元素掃一次之後再把字典裡的每個元素放進桶子裡面一樣需要O(n)時間
                最後再從桶子的最後一個開始遍歷append k次之後return result 也是O(n)
                所以複雜度是O(3n)=O(n) 
Space complexity:創建了一個長度為n的桶子list  因爲頻率次數可能為1~n 共O(n)
                之後再創建一個字典計算出每個元素出現的頻率字典的space 也是O(N) 
                之後再把top k most frequency element append到result 裡面 k最多為n 也是O(n)
                所以space：O(3n)=O(n)
"""

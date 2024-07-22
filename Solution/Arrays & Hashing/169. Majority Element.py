class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter=Counter(nums)
        return max(counter.keys(),key=counter.get)

    """
    time:O(n) counter 需要先遍歷整個array一次 計算出each element 出現的次數 找出最大值需要O(k) 另K為有K種不同數字 不會超過數組本身的N i.e. total=O(n)+O(k)<=O(2n)=O(n)
    space:O(n) 最多有n種不同的數字
    """



    """
    def majorityElement(self, nums: List[int]) -> int:
        count=0
        num=0
        hash_table={}
        for i in nums:
            hash_table[i]=hash_table.get(i,0)+1
            if hash_table[i]>count:
                num=i
                count=hash_table[i]
        return num
        """

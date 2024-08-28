class Solution:
    """
    time:O(n) list轉成set需要O(n) 從set轉回list 也須要O(n)
    space:O(n) 若初始list沒有重複元素 相當於會創建一個size=n 的list 
    """
    def thirdMax(self, nums: List[int]) -> int:
        array=list(set(nums))
        if len(array)<3:
            return max(array)
        array.sort()
        return array[-3]

class Solution:
    """
    time:O(n)
    time:O)(n)
    """
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        postive=0
        negetive=1
        n=len(nums)
        arr=[0]*n
        for i in nums:
            if i > 0:
                arr[postive]=i
                postive+=2
            else:
                arr[negetive]=i
                negetive+=2
        return arr

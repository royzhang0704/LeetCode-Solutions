class Solution:
    """
    assume len(nums1)=n1 , len(nums2)=n2
    time:O(n1+n2) 
    space:O(n1+n2) 
    """
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set(nums1)
        set2=set(nums2)
        return set(set1.intersection(set2))

"""
time:O(nlogn)
space:O(n)
"""
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        result=sorted(zip(names,heights),key=lambda x:x[1],reverse=True)
        return [name for name,height in result]

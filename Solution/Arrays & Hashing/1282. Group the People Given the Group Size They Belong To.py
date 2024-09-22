class Solution:
    """
    time:O(n) 每個元素都會遍歷一次 並且去查找當前值是否在table Search 需要O(1) total=O(n)
    space:O(n) 會包含每個元素的index total:O(n)
    """
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        table={}
        result=[]
        for index,value in enumerate(groupSizes):
            if value not in table:
                table[value]=[]
            table[value].append(index)
            
            if len(table[value])==value:
                result.append(table[value])
                table[value]=[]
        return result

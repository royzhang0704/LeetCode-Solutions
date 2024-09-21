class Solution:
    """
    time:O(n)    n為兩數組中長度較大的值
    space:O(n) n為兩數組中長度較大的值
    """
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        table1=Counter(words1)
        table2=Counter(words2)
        return sum(1 for i in table1 if table1[i]==1 and table2[i]==1 )

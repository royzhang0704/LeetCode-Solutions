class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
       return max([sum(element) for element in accounts])
        

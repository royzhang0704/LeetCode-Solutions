class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
       jewels=set(jewels)
       return sum(element in jewels for element in stones)

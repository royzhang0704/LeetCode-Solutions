class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if sum(costs)<=coins:
            return len(costs)
        if min(costs)>coins:
            return 0
        ans=0
        costs.sort()
        for i in range(len(costs)):
            if coins >=costs[i]:
                coins-=costs[i]
            else:
                return i
            

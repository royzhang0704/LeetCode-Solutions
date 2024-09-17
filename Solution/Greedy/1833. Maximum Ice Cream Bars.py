class Solution:
    """
    time:O(nlogn):排序O(nlogn)+貪心 從最小價位開始拿
    space:O(n) 排序產生得額外空間
    """
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
            

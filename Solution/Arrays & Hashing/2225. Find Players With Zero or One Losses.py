class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        ans0=[]
        ans1=[]
        player=set()
        lose=defaultdict(int)
        
        for winner,loser in matches:
            player.add(winner)
            player.add(loser)
            lose[loser]+=1

        for i in player:
            if i not in lose:
                ans0.append(i)
            elif lose[i]==1:
                ans1.append(i)
        ans0.sort()
        ans1.sort()
        
        return [ans0,ans1]

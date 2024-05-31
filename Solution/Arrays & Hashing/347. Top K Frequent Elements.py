class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq={}
        for i in nums:
            num_freq[i]=num_freq.get(i,0)+1


        pq=[]
        for entry in num_freq.items():
            heapq.heappush(pq,(entry[1],entry[0]))
            if len(pq)>k:
                heapq.heappop(pq)


        result=[]

        for i in range(k-1,-1,-1):
            result.append(heapq.heappop(pq)[1])

        return result[::-1]
                

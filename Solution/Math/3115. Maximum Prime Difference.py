class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        prime=[]
        for i in range(2,101):
            is_prime=True
            for j in range(2,int(i**0.5)+1):
                if i%j==0:
                    is_prime=False
                    break
            if is_prime:
                prime.append(i)
        result=[]
        for index,num in enumerate(nums):
            if num in prime:
                result.append(index)
        return result[-1]-result[0] if len(result)>1 else 0

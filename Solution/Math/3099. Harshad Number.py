class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        ans=0
        for i in str(x):
            ans+=int(i)
        return ans if x%ans==0 else -1

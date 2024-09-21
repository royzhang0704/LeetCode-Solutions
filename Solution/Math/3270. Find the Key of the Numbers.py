class Solution:
    """
    time:O(log min(num1,num2,num3) 處理位數時間需要花logn的時間  而while 迴圈在某數為0就會停止 因為他的前導都會是0 雨其他數取最小值結果還是0 while 迴圈次數取決於最小數
    space:O(1)
    """
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        ans=0
        pow10=1
        while num1 and num2 and num3:
            ans+=min(num1%10,num2%10,num3%10)*pow10
            num1//=10
            num2//=10
            num3//=10
            pow10*=10
        return ans

"""

0001
0010
1000
ans+=0
"""

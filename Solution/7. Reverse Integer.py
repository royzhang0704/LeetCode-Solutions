class Solution:
    def reverse(self, x: int) -> int:
        if x < -(2**31) or x > 2**31 - 1:
            return 0
        if x < 0:
            return -self.reverse(-x)  
        result = 0
        while x > 0:
            result = result * 10 + x % 10
            x //= 10
        if result < -(2**31) or result > 2**31 - 1:  # 檢查反轉後的結果是否在範圍內
            return 0
        return result

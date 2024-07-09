class Solution:
    def getEncryptedString(self, s: str, k: int) -> str:
        result=""
        for i in range(len(s)):
            result+=s[(i+k)%len(s)]
        return result

"""
time:O(n) 遍歷整個字串長度
space:O(n) result的長度為N
"""

"""
time:O(max(r,k))
space:O(r+k) r=len(word1),k=len(word2)
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        pointer=0
        result=[]
        while pointer<len(word1) and pointer<len(word2):
            result.append(word1[pointer])
            result.append(word2[pointer])
            pointer+=1
        while pointer<len(word1):
            result.append(word1[pointer])
            pointer+=1
        while pointer<len(word2):
            result.append(word2[pointer])
            pointer+=1
        return "".join(result)

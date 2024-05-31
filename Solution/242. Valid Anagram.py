class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {} #創造兩個字典 之後把字串對應的

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)# 字典的key為s[i] 對應的value 先用get看是否存在這個key 若存在就返回他對應的value 否則不存在value=0
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT #若兩個字點的key都一樣 且每個key對應的value也都一樣 代表兩字串出現的字母及字母個數都一樣

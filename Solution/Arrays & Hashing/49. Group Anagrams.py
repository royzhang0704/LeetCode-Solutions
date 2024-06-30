class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams=defaultdict(list)
        for s in strs:
            anagrams[''.join(sorted(s))].append(s)
        return list(anagrams.values())
    """
time:O(n*mlogm):n為元素個素 m元素的字傳長度 每個元素進行排序需要mlogm的時間 共n個元素
space:O(nm):最多每個元素的排序都不一樣 要有n個key的dictionary 且key的長度為m total:mn
    """

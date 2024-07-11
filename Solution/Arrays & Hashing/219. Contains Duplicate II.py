class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Approach 2024.07.08
        cache = dict()
        for i, n in enumerate(nums):
            if n in cache:
                if abs(cache[n] - i) <= k:
                    return True
            cache[n] = i
        return False


"""
time complexity:O(n) 每個元素遍歷一次 並查找在字典中是否存在 若存在且index相差<=k 查找過程只需要O(1) etc O(n)
space complexity:O(n) 創建一個大小為arr size相同的字典 O(n)
"""

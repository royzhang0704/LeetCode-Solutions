class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # 創建一個排序好的數組
        nums_sort = sorted(nums)
        # 建立字典，key:數字 value:該數字在排序數組中的第一個出現的索引
        nums_count = {}
        for index, value in enumerate(nums_sort):
            if value not in nums_count:  # 處理重複的數字
                nums_count[value] = index
        # 使用理解列表生成結果
        result = [nums_count[value] for value in nums]
        return result

"""
time complexity: O(n log n)
先把數組排序需要 O(n log n) 時間
再去查詢每個元素在字典裡的 key，共有 n 次查詢，每次查詢需要 O(1) 時間
總時間複雜度 = O(n log n + n * O(1)) = O(n log n)

space complexity: O(n)
最多 n 個不同元素，需要大小為 n 的字典
排序數組也需要 O(n) 的空間
結果列表需要 O(n) 的空間
總空間複雜度 = O(n)
"""

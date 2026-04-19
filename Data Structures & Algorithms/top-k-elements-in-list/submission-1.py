class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = Counter(nums)
        return sorted(res, key = lambda x: res[x], reverse = True)[:k]
        
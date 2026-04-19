class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        res = {}

        for i, n in enumerate(nums):
            if n in res:
                res[n] += 1
            else:
                res[n] = 1
        
        sorted_res = sorted(res, key = lambda x: res[x], reverse = True)
        return sorted_res[:k]
        
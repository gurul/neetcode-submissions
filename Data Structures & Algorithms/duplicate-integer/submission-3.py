class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        size = len(nums)
        uniqueN = set(nums)
        return (size > len(uniqueN))
        
        
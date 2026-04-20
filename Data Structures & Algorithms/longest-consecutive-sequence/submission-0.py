class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        starters = []

        for i in range(len(nums)):
            if (nums[i] - 1) not in numSet:
                starters.append(nums[i])
        
        longest = 0

        for start in starters:
            length = 1
            while (start + length) in numSet:
                length += 1
            longest = max(longest, length)
        
        return longest
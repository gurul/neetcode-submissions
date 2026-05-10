class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        nested for loop to find a repeat O(n^2)

        1 pass approach: using a set

        init set
        for i in length:
            if value in set: return false
            set.add(value)
        return true
        """
        values = set()
        for num in nums:
            if num in values: return True
            values.add(num)
        return False
        
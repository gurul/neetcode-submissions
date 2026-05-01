class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2          # ① integer division
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                hi = mid - 1              # ② search left half
            else:
                lo = mid + 1              # ③ search right half

        return -1                         # ④ not found
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        O(n) time complextity
        O(n) space complexity

        n = len(nums)

        prefix = [1] * n
        postfix = [1] * n
        out = [0] * n

        for i in range(1, n):
            prefix[i] = prefix[i-1] * nums[i-1]

        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]

        for i in range(n):
            out[i] = prefix[i] * postfix[i]

        return out
        """

        n = len(nums)
        out = [1] * n

        for i in range (1, n):
            out[i] = out[i-1] * nums[i-1]

        postfix = 1
        for i in range(n - 2, -1, -1):
            postfix *= nums[i+1]
            out[i] *= postfix

        return out








        
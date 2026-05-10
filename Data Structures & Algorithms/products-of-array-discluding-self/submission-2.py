class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        brute force approach: multiply all, divide by pos

        productL = 1
        for left to right starting at 1:
            productL *= the one to the left of the current element
            currEl = productL
        
        productR = 1
            for right to left starting from second to end"
            productR *= the one to the right of the current element
            current = productR
        
        return nums

        1 1 1 1
        2 3 4 5

        lPass = 1 2 6 24


        """
        productLPass = [1] * len(nums)
        productRPass = [1] * len(nums)
        for i in range(1,len(nums)):
            productLPass[i] *= nums[i - 1] * productLPass[i - 1]

        for i in range(len(nums) - 2, -1, -1):
            productRPass[i] *= nums[i+1] * productRPass[i+1]
        
        for i in range(len(nums)):
             productLPass[i] *= productRPass[i]
        
        return productLPass
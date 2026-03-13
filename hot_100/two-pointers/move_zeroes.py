from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        l = r = 0
        while r < n:
            if nums[r] != 0:
                nums[l],nums[r] = nums[r],nums[l]
                l += 1
            r += 1
        return nums
    

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        j = 0 
        if not nums:
            return 0
        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
            i += 1
        for i in range(j,n):
            nums[i] = 0
        return nums
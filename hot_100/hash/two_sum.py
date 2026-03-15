from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            j = target - i
            start = nums.index(i)
            next = start + 1
            temp_nums = nums[next:]
            if j in temp_nums:
                return(nums.index(i),next + temp_nums.index(j))

#hash
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for i,num in enumerate(nums):
            if target - num in hash:
                return [ hash[target - num], i ]
            hash[nums[i]] = i

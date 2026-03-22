from typing import List
#建立集合 哈希
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = 0
        if 1 not in nums:
            return 1
        else:
            set_nums = set(nums)
            for i in set_nums:
                if i >= 1:
                    n += 1

            for i in range(1 , n + 2):
                if i not in set_nums:
                    return i
                    
#原地哈希
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        #将所有小于等于0的数和大于n的数替换为n+1
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1
        #将nums[i]对应的索引位置的数变为负数，表示该索引位置的数存在
        for i in range(n):
            num = abs(nums[i])
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])
        #遍历数组，找到第一个正数的位置，该位置的索引加1就是缺失的最小正数
        for i in range(n):
            if nums[i] > 0:
                return i + 1
        return n + 1
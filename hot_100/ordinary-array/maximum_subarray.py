from typing import List
#暴力破解，超时
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        #计算前缀和
        nums_n = [0] * (n + 1)
        for i in range(n):
            nums_n[i + 1] = nums_n[i] + nums[i]
        #设为负无穷而不是0，避免最大值为负数时返回0
        max_sum = float('-inf')
        #暴力破解，遍历前缀和相减的每一种组合
        for i in range(n):
            for j in range(i , n):
                current_sum = nums_n[j + 1] - nums_n[i]
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum
                
        

#动态规划
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #计算前缀和，但是当前缀和为负数时，重新开始计算前缀和
        for i in range(1, len(nums)):
            nums[i] += max(nums[i - 1] , 0)
        #返回前缀和的最大值
        return max(nums)
                
        
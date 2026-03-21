from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #计算数组长度，初始化answer
        n = len(nums)
        answer = [0]*n
        answer[0] = 1
        #计算answer[i]为nums[0]到nums[i-1]的乘积
        for i in range(1, n):
            answer[i] = answer[i - 1] *nums[i - 1]
        #计算R为nums[i+1]到nums[n-1]的乘积，并将answer[i]乘以R
        R = 1
        while i >= 0:
            answer[i] = answer[i] *R
            R *= nums[i]
            i -= 1
        return answer
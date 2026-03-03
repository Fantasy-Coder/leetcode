from typing import List
#两数之和的函数
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #从第一个数开始遍历
        for i in nums:
            #计算出另一个数的数值
            j = target - i
            #记录开始的索引及下一个索引
            start_index = nums.index(i)
            next_index  = start_index + 1
            #暂存从下一个索引开始的列表
            temp_nums = nums[next_index:]
            #如果数字在列表中则返回两个数的索引
            if j in temp_nums:
                return(nums.index(i),next_index + temp_nums.index(j))
 #自己输入测试用例
nums = input("Enter the list of numbers (comma separated): ")
nums = [int(x.strip()) for x in nums.split(",")]
target = int(input("Enter the target number: "))
solution = Solution()
print("Input: nums =", nums, ", target =", target)
print("Output:", solution.twoSum(nums, target))
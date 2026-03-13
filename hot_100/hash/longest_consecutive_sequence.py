from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #最长连续序列的长度
        longest_streak = 0
        #将输入的列表转换为集合，以便快速查找
        num_set = set(nums)
        #遍历集合中的每一个数字
        for num in num_set:
            #如果当前数字的前一位没有数字，说明当前数字可能是序列起点
            if num - 1 not in num_set:      
                current_num = num
                current_streak = 1
                #继续检查当前数字的后一位是否存在，如果存在则继续增加当前序列的长度
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                longest_streak = max(longest_streak,current_streak)
        return longest_streak
        
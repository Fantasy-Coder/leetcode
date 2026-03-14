class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        #排序
        nums.sort()
        ans = list()
        #枚举first
        for first in range(n):
            #去重
            if first > 0 and nums[first] == nums[first - 1]:
                continue
            #使用双指针枚举second和third
            third = n - 1
            #确定target
            target = -nums[first]
            #枚举second
            for second in range(first + 1,n):
                #去重
                if second > first + 1 and nums[second] == nums[second -1]:
                    continue
                #移动third指针
                while second < third and nums[second] + nums[third] > target:
                    third -= 1
                #如果指针重合，随着second后续的增加，third一定会再减小，所以可以退出循环
                if second == third:
                    break
                #找到答案
                if nums[second] + nums[third] == target:
                    ans.append([nums[first],nums[second],nums[third]])
        return ans
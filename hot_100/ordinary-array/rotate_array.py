from typing import List
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #将后k个元素保存到临时列表中
        n = len(nums)
        #取模，防止k大于n的情况
        k = k % n
        temp = []
        temp = nums[n - k : n]
        i = n - k - 1
        #将前n-k个元素向后移动k个位置
        while i >= 0:
            nums[i + k] = nums[i]
            i -= 1
        #将临时列表中的元素复制回原列表的前k个位置
        for i in range(k):
            nums[i] = temp[i]
        return nums
    

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #反转整个数组，再将前k个元素反转，最后将后n-k个元素反转
        #取模，防止k大于n的情况
        k = k % len(nums)
        nums.reverse()
        nums[:k] = reversed(nums[:k])
        nums[k:] = reversed(nums[k:])

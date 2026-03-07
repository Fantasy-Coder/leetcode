from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) % 2 == 1:
            return nums[(len(nums))//2]
        else:
            return (nums[len(nums)//2-1] + nums[len(nums)//2]) / 2
        
#二分法
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 计算两个数组的长度和总长度
        m = len(nums1)
        n = len(nums2)
        totalLength = m + n
        # 定义函数，找到两个有序数组中第 k 小的元素，此题k为中位数的位置
        def getKthElement(k):
            # 两个数组的当前查找起始位置
            index1 = index2 = 0
            while True:
                # 边界1：nums1已遍历完，直接返回nums2中剩余部分的第k个元素
                if index1 == m:
                    return nums2[index2 + k -1]
                # 边界2：nums2已遍历完，直接返回nums1中剩余部分的第k个元素
                if index2 == n:
                    return nums1[index1 + k -1]
                # 边界3：找第1小的元素，直接返回两个数组当前起始位置的较小值
                if k == 1:
                    return min(nums1[index1],nums2[index2])
                # 计算本次要比较的位置（避免越界）
                newindex1 = min(index1 + k // 2 - 1,m - 1)
                newindex2 = min(index2 + k // 2 - 1,n - 1)
                pivot1,pivot2 = nums1[newindex1],nums2[newindex2]
                # 核心二分：排除不可能的元素，缩小查找范围
                if pivot1 <= pivot2:
                     # nums1中[index1, newindex1]的元素都小于等于pivot2，不可能是第k小
                    k -= newindex1 - index1 + 1   # 剩余要找的k值减少
                    index1 = newindex1 + 1  # nums1的查找起始位置后移
                else:
                    # nums2中[index2, newindex2]的元素都小于pivot1，同理排除
                    k -= newindex2 - index2  + 1
                    index2 =newindex2 + 1
        # 根据总长度的奇偶性，计算中位数
        if totalLength % 2 == 1:
            return getKthElement((totalLength + 1) // 2)
        else:
            return (getKthElement(totalLength // 2) + getKthElement(totalLength // 2 + 1)) / 2

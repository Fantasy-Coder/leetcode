from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        l = 0
        r = n -1
        hr = hl = 0
        max_areas = areas = 0
        #双指针
        while r > l:
            hr,hl = height[r],height[l]
            #计算当前面积
            areas = (r - l)*min(hr,hl)
            #更新最大面积
            if areas > max_areas:
                max_areas = areas
            #移动较短的指针    
            if hr > hl:
                l += 1
            else:
                r -= 1
        return max_areas
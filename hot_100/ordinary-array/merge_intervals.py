from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        #根据小列表的第一个数进行排序（即区间的左边界）
        intervals.sort(key = lambda x:x[0])
        
        merged = []
        #遍历排序后的区间列表
        for interval in intervals:
            #如果结果列表为空，或者结果列表的最后一个区间的右边界小于当前区间的左边界
            if not merged or merged[-1][1] < interval[0]:
                #将当前区间添加到结果列表中
                merged.append(interval)
            else:
                #否则，结果列表的最后一个区间的右边界更新为当前区间的右边界和结果列表的最后一个区间的右边界的较大值
                merged[-1][1] = max(merged[-1][1] , interval[1])
        return merged
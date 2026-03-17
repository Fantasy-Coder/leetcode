from collections import defaultdict
from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 前缀和 + 哈希表
        #初始化前缀和数组，其中s[0] = 0
        s = [0] * (len(nums) + 1)
        #计算前缀和
        for i, x in enumerate(nums):
            s[i + 1] = s[i] + x
        #使用哈希表统计前缀和出现的次数
        cnt = defaultdict(int)
        ans = 0
        #遍历前缀和数组，对于每个前缀和sj，统计之前出现过的前缀和sj - k的次数，并将当前前缀和sj加入哈希表中
        for sj in s:
            ans += cnt[sj - k]
            cnt[sj] += 1
        return ans


from typing import List
import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #默认值为列表的字符mp，key：排序后的字符串，value：对应的原始字符串列表
        mp = collections.defaultdict(list)
        #遍历每一个字符串
        for st in strs:
            #对字符串进行排序，再拼接成新字符串
            key = "".join(sorted(st))
            #将当前字符串添加到对应键的列表中
            mp[key].append(st)
        #将字典中所有的值，转换为列表格式返回
        return list(mp.values())


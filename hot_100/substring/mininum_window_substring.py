from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #初始化计时器
        cnt_s = Counter()
        cnt_t = Counter(t)
        #初始化结果窗口
        ans_left , ans_right = -1 , len(s)
        #左指针初始为0
        left = 0
        #遍历右指针的字符
        for right , c in enumerate(s):
            #使该字符计数器+1
            cnt_s[c] += 1
            #对每一个t内的字符，s的计数器都比t大
            while cnt_s >= cnt_t:
                #如果当前窗口的大小小于结果窗口，则重新赋值结果窗口
                if right - left < ans_right - ans_left:
                    ans_left , ans_right = left , right
                #将左指针右移，左指针的字符的计数器-1
                cnt_s[s[left]] -= 1
                left += 1
        #返回结果
        return "" if ans_left < 0 else s[ans_left: ans_right + 1]


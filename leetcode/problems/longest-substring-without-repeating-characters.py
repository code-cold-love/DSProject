# -*- coding: utf-8 -*-
# 3. 无重复字符的最长子串 https://leetcode.cn/problems/longest-substring-without-repeating-characters/
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0 or n == 1:
            return n
        right = -1  # 右指针，子串的结束位置
        ans, occ = 0, set()
        for left in range(n):
            if left != 0:  # 左指针向右移动一格，哈希集合移除一个字符
                occ.remove(s[left - 1])
            while right + 1 < n and s[right + 1] not in occ:
                right += 1  # 不断地移动右指针
                occ.add(s[right])
            ans = max(ans, right - left + 1)
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.lengthOfLongestSubstring('abcabcbb'))  # 3

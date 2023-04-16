# -*- coding: utf-8 -*-
# 784. 字母大小写全排列 https://leetcode.cn/problems/letter-case-permutation/
from typing import List
from collections import deque


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        # s 由小写英文字母、大写英文字母和数字组成
        ans = []

        def backtrack(s_list: List[str], pos: int) -> None:
            n = len(s_list)
            while pos < n and s_list[pos].isdigit():
                pos += 1
            if pos == n:
                ans.append(''.join(s_list))
                return
            backtrack(s_list, pos + 1)
            s_list[pos] = s_list[pos].swapcase()
            backtrack(s_list, pos + 1)
            s_list[pos] = s_list[pos].swapcase()  # 恢复

        backtrack(list(s), 0)
        return ans

    def letterCasePermutation_bfs(self, s: str) -> List[str]:
        n, ans = len(s), []
        q = deque([''])
        while q:
            cur = q[0]
            pos = len(cur)
            if pos == n:
                ans.append(cur)
                q.popleft()
            else:
                if s[pos].isalpha():
                    q.append(cur + s[pos].swapcase())  # 加上交换形式后的
                q[0] += s[pos]  # 加上交换形式前的和数字字符
        return ans


if __name__ == '__main__':
    obj = Solution()
    print(obj.letterCasePermutation('a1b2'))
    print(obj.letterCasePermutation_bfs('a1b2'))

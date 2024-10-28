#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 93. 复原 IP 地址 https://leetcode.cn/problems/restore-ip-addresses/
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # 切割问题，参考 131. 分割回文串
        ans = []

        def backtrack(sb: str, start: int, path: list) -> None:
            if start == len(sb) and len(path) == 4:
                ans.append('.'.join(path))
                return
            elif len(path) > 4:  # 剪枝
                return

            # 单层处理
            for i in range(start, min(start + 3, len(sb))):
                if self.is_valid(sb, start, i):
                    sub = sb[start:i + 1]  # 处理节点
                    path.append(sub)
                    backtrack(sb, i + 1, path)  # 递归
                    path.pop()  # 回溯

        backtrack(s, 0, [])
        return ans

    @staticmethod
    def is_valid(s: str, start: int, end: int) -> bool:
        if start > end:
            return False
        elif s[start] == '0' and start != end:
            # 0 开头的数字不合法
            return False
        num = int(s[start:end + 1])
        return 0 <= num <= 255


if __name__ == '__main__':
    obj = Solution()
    print(obj.restoreIpAddresses('25525511135'))  # ['255.255.11.135', '255.255.111.35']
    print(obj.restoreIpAddresses('0000'))  # ['0.0.0.0']
    print(obj.restoreIpAddresses('101023'))  # ['1.0.10.23', '1.0.102.3', '10.1.0.23', '10.10.2.3', '101.0.2.3']

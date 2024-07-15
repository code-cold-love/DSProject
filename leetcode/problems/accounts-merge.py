#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 721. 账户合并 https://leetcode.cn/problems/accounts-merge/
from typing import List
from collections import defaultdict


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # 哈希 + DFS
        email_to_idx_of_name = defaultdict(list)  # key 为邮箱地址，value 为这个邮箱对应的账户下标
        for i, account in enumerate(accounts):
            for e in account[1:]:
                email_to_idx_of_name[e].append(i)

        def dfs(idx: int) -> None:
            visited[idx] = True
            for email in accounts[idx][1:]:
                if email in emails:
                    continue
                emails.add(email)
                for j in email_to_idx_of_name[email]:
                    if not visited[j]:
                        dfs(j)

        ans = []
        visited = [False] * len(accounts)
        for i, v in enumerate(visited):
            if not v:  # 下标 i 代表的账户没有访问过
                emails = set()  # 收集 DFS 中访问的邮箱地址
                dfs(i)
                ans.append([accounts[i][0]] + sorted(emails))
        return ans


if __name__ == '__main__':
    solution = Solution()
    # [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'], ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
    print(solution.accountsMerge([["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
                                  ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]))

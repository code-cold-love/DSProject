# -*- coding: utf-8 -*-
# 468. 验证IP地址 https://leetcode.cn/problems/validate-ip-address/
import re


class Solution:
    def validIPAddress(self, query_ip: str) -> str:
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', query_ip):
            ips = query_ip.split('.')
            for i in ips:
                int_i = int(i)
                if int_i < 0 or int_i > 255 or len(i) != len(str(int_i)):
                    return 'Neither'
            return 'IPv4'
        elif re.match(r'^[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}:[\da-fA-F]{1,4}$', query_ip):
            return 'IPv6'
        return 'Neither'


if __name__ == '__main__':
    obj = Solution()
    print(obj.validIPAddress('172.16.254.1'))  # IPv4
    print(obj.validIPAddress('2001:0db8:85a3:0:0:8A2E:0370:7334'))  # IPv6
    print(obj.validIPAddress('256.256.256.256'))  # Neither

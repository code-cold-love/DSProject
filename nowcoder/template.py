# -*- coding: utf-8 -*-
import sys

if __name__ == '__main__':
    for line in sys.stdin:
        a = line.split()
        print(int(a[0]) + int(a[1]))

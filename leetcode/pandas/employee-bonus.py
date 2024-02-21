#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 577. 员工奖金 https://leetcode.cn/problems/employee-bonus/
import pandas as pd


def employee_bonus(employee: pd.DataFrame, bonus: pd.DataFrame) -> pd.DataFrame:
    merged_df = pd.merge(employee, bonus, how='left', on='empId')
    mask = (merged_df['bonus'] < 1000) | (merged_df['bonus'].isna())
    result_df = merged_df[mask][['name', 'bonus']]
    return result_df


if __name__ == '__main__':
    data = [[3, 'Brad', None, 4000], [1, 'John', 3, 1000], [2, 'Dan', 3, 2000], [4, 'Thomas', 3, 4000]]
    employee = pd.DataFrame(data, columns=['empId', 'name', 'supervisor', 'salary']).astype(
        {'empId': 'Int64', 'name': 'object', 'supervisor': 'Int64', 'salary': 'Int64'})

    data = [[2, 500], [4, 2000]]
    bonus = pd.DataFrame(data, columns=['empId', 'bonus']).astype({'empId': 'Int64', 'bonus': 'Int64'})
    print(employee_bonus(employee, bonus))

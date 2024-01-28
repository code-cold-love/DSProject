# -*- coding: utf-8 -*-
# 177. 第N高的薪水 https://leetcode.cn/problems/nth-highest-salary/
import pandas as pd


def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    df = employee[['salary']].drop_duplicates()
    if len(df) < N:
        return pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [None]})
    df = df.sort_values(ascending=False, by='salary').head(N).tail(1)
    return df.rename(columns={'salary': 'getNthHighestSalary(' + str(N) + ')'})


if __name__ == '__main__':
    data = [[1, 100], [2, 200], [3, 300]]
    employee = pd.DataFrame(data, columns=['id', 'salary']).astype({'id': 'Int64', 'salary': 'Int64'})
    print(nth_highest_salary(employee, 2))

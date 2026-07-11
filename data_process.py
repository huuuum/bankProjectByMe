from email.policy import default

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 基础数据探索
cust_df = pd.read_csv('data/cust_info.csv')
loan_df = pd.read_csv('data/loan_info.csv')
#
# print('用户表前五行：\n',cust_df.head())
# print('用户表基础信息：\n',cust_df.info())
#
# print('贷款表前五行：\n',loan_df.head())
# print('贷款表基础信息：\n',loan_df.info())
# print('贷款表数值字段统计：\n',loan_df[["loan_amount", "overdue_days", "is_default"]].describe())
#
# default_rate = loan_df['is_default'].mean()
# print(f'\n贷款违约率：{default_rate:.2%}')
#
# 重复值处理
print('用户表缺失值数量：',cust_df.duplicated().sum())
print('贷款表缺失值数量：',loan_df.duplicated().sum())
print('用户表id缺失值数量：',cust_df.duplicated(subset=['cust_id']).sum())
print('贷款表id缺失值数量：',loan_df.duplicated(subset=['loan_id']).sum())

cust_df = cust_df.drop_duplicates(keep='first')
loan_df = loan_df.drop_duplicates(keep='first')
cust_df = cust_df.drop_duplicates(subset=['cust_id'],keep='first')
cust_df = loan_df.drop_duplicates(subset=['loan_id'],keep='first')


# 缺失值处理
print('用户表缺失值：',cust_df.isna().sum())
print('贷款表缺失值：',loan_df.isna().sum())

# 异常值处理
loan_df = loan_df[loan_df["loan_amount"] > 0 ]
loan_df = loan_df[loan_df["overdue_days"] >= 0 ]

full_df = pd.merge(loan_df,cust_df,on='cust_id',how='left')
full_df.to_csv('data/full_info.csv',index=False,encoding='utf-8-sig')

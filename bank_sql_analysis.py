import pandas as pd
from sqlalchemy import create_engine
import matplotlib as plt

plt.rcParams["font.sans-serif"] = ["SimHei"]
plt.rcParams["axes.unicode_minus"] = False

user = 'root'
password = 'okb13950958240'
port = 3306
database = 'bank_data'
host = 'localhost'

engine = create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=utf8mb4')

sql_total_default = """
SELECT
    COUNT(loan_id) AS total_loan_count,
    SUM(is_default) AS total_is_default,
    ROUND(SUM(is_default) / COUNT(loan_id),4) AS default_rate
FROM full_info;
"""
df_total_default = pd.read_sql(sql_total_default,engine)
df_total_default['default_rate'] = df_total_default['default_rate'].apply(lambda x : f'{x:.2%}')
print('\n---------整体违约率----------')
print(df_total_default)

sql_type_default = """
SELECT
    loan_type,
    COUNT(loan_id) AS total_loan_count,
    SUM(is_default) AS total_is_default,
    SUM(loan_amount) AS total_loan_amount,
    ROUND(SUM(is_default) / COUNT(loan_id),4) AS default_rate,
    ROUND(AVG(loan_amount),0) AS avg_loan_amount
FROM full_info GROUP BY loan_type;
"""

df_type_default = pd.read_sql(sql_type_default,engine)
df_type_default['default_rate'] = df_type_default['default_rate'].apply(lambda x : f'{x:.2%}')
df_type_default['avg_loan_amount'] = df_type_default['avg_loan_amount'].apply(lambda x : f'{x / 10000:.1f}万元')
print('\n---------按类型分类----------')
print(df_type_default)

sql_level_default = """
SELECT 
    cust_level,
    COUNT(loan_id) AS total_loan_count,
    SUM(is_default) AS total_is_default,
    SUM(loan_amount) AS total_loan_amount,
    ROUND(SUM(is_default) / COUNT(loan_id),4) AS default_rate,
    ROUND(AVG(loan_amount),0) AS avg_loan_amount
    FROM full_info GROUP BY cust_level;
"""

df_level_default = pd.read_sql(sql_level_default,engine)
df_level_default['default_rate'] = df_level_default['default_rate'].apply(lambda x : f'{x:.2%}')
df_level_default['avg_loan_amount'] = df_level_default['avg_loan_amount'].apply(lambda x : f'{x / 10000:.1f}万元')
print('\n---------按等级分类----------')
print(df_level_default)

sql_age_default = """
SELECT 
    age_group,
    COUNT(loan_id) AS total_loan_count,
    COUNT(loan_id) AS total_loan_count,
    SUM(is_default) AS total_is_default,
    SUM(loan_amount) AS total_loan_amount,
    ROUND(SUM(is_default) / COUNT(loan_id),4) AS default_rate,
    ROUND(AVG(loan_amount),0) AS avg_loan_amount
    FROM full_info GROUP BY age_group;
"""
df_age_default = pd.read_sql(sql_age_default,engine)
df_age_default['default_rate'] = df_age_default['default_rate'].apply(lambda x : f'{x:.2%}')
df_age_default['avg_loan_amount'] = df_age_default['avg_loan_amount'].apply(lambda x : f'{x / 10000:.1f}万元')
print('\n---------按年龄分类----------')
print(df_age_default)

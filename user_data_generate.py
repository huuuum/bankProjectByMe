import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(42)
cust_count = 1000
cust_data = {
    "cust_id":[f"C{str(i).zfill(6)}" for i in range(1,cust_count+1)],
    "age":[np.random.randint(18,71,size=cust_count)],
    "income":[np.random.randint(100,10000,size=cust_count)*10],
    "education":[np.random.choice(['大专及以下','本科','研究生及以上'],size=cust_count,p=(0.6,0.3,0.1))],
    "cust_level":[np.random.choice(['普通','金卡','钻石'],size=cust_count,p=(0.7, 0.25, 0.05))],
    "register_years":[np.random.randint(2000,2026,size=cust_count)],
}
cust_df = pd.DataFrame(cust_data)
cust_df.to_csv('cust_info.csv',index=False,encoding='utf-8-sig')
print('用户信息表生成完毕')
print('用户表前十行数据：',cust_df.head(10))
print('用户表形状：',cust_df.shape)

loan_count = 1200
loan_data = {
    "loan_id":[f"L{str(i).zfill(6)}"for i in range(1,loan_count+1)],
    "cust_id":[np.random.choice(cust_df['cust_id'],size=loan_count)]

}
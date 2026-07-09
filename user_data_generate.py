import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

np.random.seed(42)
cust_count = 1000
cust_data = {
    "cust_id":[f"C{str(i).zfill(6)}" for i in range(1,cust_count+1)],
    "age":[np.random.randint(18,71)],
    "income":[np.random.randint(100,10000)*10],
    "education":[np.random.choice(['大专及以下','本科','研究生及以上'],size=cust_count,p=(0.6,0.3,0.1))],
}
cust_df = pd.DataFrame(cust_data)
#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import statistics

# Load the data
df_stock = pd.read_excel(file_path, sheet_name='IRCTC Stock Price')

# Extract the Price data
price_data = df_stock['Price'].dropna()

# Calculate mean and variance
mean_price = statistics.mean(price_data)
variance_price = statistics.variance(price_data)

print(f"Mean Price: {mean_price}")
print(f"Variance Price: {variance_price}")


# In[ ]:





#!/usr/bin/env python
# coding: utf-8

# <a href="https://colab.research.google.com/github/deva-kumari/devakumari_cse22237/blob/main/A4-B.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# In[19]:


# Convert 'Date' column to datetime
df_stock['Date'] = pd.to_datetime(df_stock['Date'])

# Filter price data for Wednesdays
wednesdays = df_stock[df_stock['Date'].dt.day_name() == 'Wednesday']
wednesday_prices = wednesdays['Price']

# Calculate sample mean for Wednesdays
mean_wednesday_price = statistics.mean(wednesday_prices)

# Compare with population mean
print(f"Mean Price on Wednesdays: {mean_wednesday_price}")
print(f"Population Mean Price: {mean_price}")


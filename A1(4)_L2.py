#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# Load the data
file_path = 'C:/Users/year3/Downloads/L2_data.xlsx'
df = pd.read_excel(file_path, sheet_name='Purchase data')

# Clean the data
df_cleaned = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)', 'Payment (Rs)']].dropna()

# Extract features and target variable
A = df_cleaned.iloc[:, :-1].values  # Product quantities
C = df_cleaned.iloc[:, -1].values   # Payment

# Ensure A and C are numeric numpy arrays
A = A.astype(np.float64)
C = C.astype(np.float64)

# Compute the pseudo-inverse of A
A_pseudo_inverse = np.linalg.pinv(A)

# Calculate the model vector X (product costs)
product_costs = np.dot(A_pseudo_inverse, C)

# Display the product costs
print("Product costs:", product_costs)


# In[ ]:





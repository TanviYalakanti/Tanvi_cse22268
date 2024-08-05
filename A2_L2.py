#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

# Load the data
file_path = 'C:/Users/year3/Downloads/L2_data.xlsx'
df = pd.read_excel(file_path, sheet_name='Purchase data')

# Print the initial DataFrame to inspect
print("Initial DataFrame:")
print(df.head())

# Select only relevant columns and drop NaN values
df_cleaned = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)', 'Payment (Rs)']].dropna()

# Print the cleaned DataFrame
print("Cleaned DataFrame:")
print(df_cleaned.head())

# Assuming the last column is the total cost (C) and the rest are product quantities (A)
A = df_cleaned.iloc[:, :-1].values  # All columns except the last one
C = df_cleaned.iloc[:, -1].values   # The last column

# Ensure A and C are numeric numpy arrays
A = A.astype(np.float64)
C = C.astype(np.float64)

# Calculate the pseudo-inverse of A
A_pseudo_inverse = np.linalg.pinv(A)

# Calculate the model vector X (cost of each product)
X = np.dot(A_pseudo_inverse, C)

# Output results
print("Pseudo-Inverse of Matrix A:")
print(A_pseudo_inverse)
print("Model Vector X (Cost of each product):")
print(X)


# In[ ]:





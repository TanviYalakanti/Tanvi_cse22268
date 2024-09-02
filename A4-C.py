#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pandas as pd

# Correctly specify the path to your Excel file
file_path = r"C:\Users\year3\Downloads\Lab Session Data.xlsx"

# Load the Excel file into a DataFrame
try:
    df = pd.read_excel(file_path)
    print("File loaded successfully.")
    print(df.head())  # Display the first few rows to verify

    # Check if 'Date' column exists
    if 'Date' in df.columns:
        df['Date'] = pd.to_datetime(df['Date'])
        print("Date column converted successfully.")

        # Extract April data
        april_data = df[df['Date'].dt.month == 4]
        print("April data extracted successfully.")
        print(april_data.head())

        # Check if 'Close' column exists
        if 'Close' in df.columns:
            april_prices = april_data['Close'].tolist()
            historical_prices = df['Close'].tolist()

            # Calculate the sample mean for April
            sample_mean_april = sum(april_prices) / len(april_prices)

            # Calculate the population mean from historical data
            population_mean = sum(historical_prices) / len(historical_prices)

            # Print the results
            print(f"Sample Mean for April: {sample_mean_april:.2f}")
            print(f"Population Mean: {population_mean:.2f}")

            # Compare the means
            if sample_mean_april > population_mean:
                print("The sample mean for April is higher than the population mean.")
            elif sample_mean_april < population_mean:
                print("The sample mean for April is lower than the population mean.")
            else:
                print("The sample mean for April is equal to the population mean.")
        else:
            print("'Close' column not found.")
    else:
        print("'Date' column not found.")

except Exception as e:
    print(f"Error: {e}")


# In[ ]:





# In[ ]:





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

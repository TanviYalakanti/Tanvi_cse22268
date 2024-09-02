import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load the data
file_path = 'C:/Users/year3/Downloads/L2_data.xlsx'
df = pd.read_excel(file_path, sheet_name='Purchase data')

# Select relevant columns and drop rows with NaN values
df_cleaned = df[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)', 'Payment (Rs)']].dropna()

# Label customers based on payment amount
df_cleaned['Class'] = df_cleaned['Payment (Rs)'].apply(lambda x: 'RICH' if x > 200 else 'POOR')

# Print class distribution
print("Class distribution in the dataset:")
print(df_cleaned['Class'].value_counts())

# Features and target
X = df_cleaned[['Candies (#)', 'Mangoes (Kg)', 'Milk Packets (#)']].values
y = df_cleaned['Class'].values

# Convert target to binary (0 for POOR, 1 for RICH)
y = np.where(y == 'RICH', 1, 0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Standardize features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
print("Accuracy Score:", accuracy_score(y_test, y_pred))
print("Classification Report:")
print(classification_report(y_test, y_pred, zero_division=0))

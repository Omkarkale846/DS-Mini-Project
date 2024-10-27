# -*- coding: utf-8 -*-
"""Copy of Welcome To Colab

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1TUFzx8RN9KFEl6Zl2zuy-nMlcUzMc_gx
"""

# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Load the dataset
df = pd.read_csv('/content/sample_data/aw_fb_data.csv')

# Display the first few rows of the dataset
print(df.head())

# Check for missing values
print(df.isnull().sum())

# Display basic statistics of the dataset
print(df.describe())

# Visualize Data
# Boxplot for visualizing outliers in Heart Rate
plt.figure(figsize=(8, 6))
sns.boxplot(x=df['heart_rate'])
plt.title('Boxplot of Heart Rate')
plt.show()

# Histogram for Step Count
plt.figure(figsize=(8, 6))
plt.hist(df['Steps'], bins=20, color='skyblue')
plt.title('Histogram of Step Count')
plt.xlabel('Steps')
plt.ylabel('Frequency')
plt.show()

# Scatter plot to visualize relationship between Steps and Calories Burned
plt.figure(figsize=(8, 6))
plt.scatter(df['Steps'], df['CaloriesBurned'], color='green')
plt.title('Scatter Plot: Steps vs Calories Burned')
plt.xlabel('Steps')
plt.ylabel('Calories Burned')
plt.show()

# Pearson Correlation Matrix
numeric_df = df.select_dtypes(include=['number'])
corr_matrix = numeric_df.corr()

# Plot the correlation heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
plt.title('Correlation Matrix')
plt.show()

# Identify Dependent and Independent features
# Independent features (Predictors): Steps, HeartRate, SleepHours
# Dependent feature (Target): CaloriesBurned
X = df[['Steps', 'heart_rate']]  # Independent features , 'SleepHours'
y = df['CaloriesBurned']  # Dependent feature

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on test data
y_pred = model.predict(X_test)

# Calculate mean squared error (MSE)
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Visualize the actual vs predicted values
plt.figure(figsize=(8, 6))
plt.scatter(y_test, y_pred, color='blue')
plt.plot([min(y_test), max(y_test)], [min(y_pred), max(y_pred)], color='red', linewidth=2)
plt.title('Actual vs Predicted Calories Burned')
plt.xlabel('Actual Calories Burned')
plt.ylabel('Predicted Calories Burned')
plt.show()
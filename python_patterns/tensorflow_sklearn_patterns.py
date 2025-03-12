import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

"""
This script provides common patterns for using TensorFlow in Machine Learning,
performing Principal Component Analysis (PCA), and handling various data science tasks including forecasting.

Topics Covered:
- Building and training a simple TensorFlow neural network
- Using PCA for dimensionality reduction
- Preprocessing data with StandardScaler
- Performing exploratory data analysis
- Implementing linear regression for forecasting
- Visualizing data trends
"""

# 1. Building and Training a Simple TensorFlow Model
def create_simple_nn(input_shape):
    """Creates a simple neural network model using TensorFlow/Keras."""
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(64, activation='relu', input_shape=(input_shape,)),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='linear')  # Linear activation for regression tasks
    ])
    
    model.compile(optimizer='adam', loss='mse', metrics=['mae'])
    return model

# 2. Principal Component Analysis (PCA)
def perform_pca(data, n_components=2):
    """Performs PCA on the given dataset and returns transformed data."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    
    pca = PCA(n_components=n_components)
    principal_components = pca.fit_transform(scaled_data)
    
    return principal_components, pca.explained_variance_ratio_

# 3. Data Analysis Example (Pandas + NumPy)
def load_and_analyze_data(csv_path):
    """Loads a CSV file into a Pandas DataFrame and performs basic analysis."""
    df = pd.read_csv(csv_path)
    print("First few rows:")
    print(df.head())
    print("\nSummary Statistics:")
    print(df.describe())
    return df

# 4. Implementing Linear Regression for Forecasting
def linear_regression_forecasting(df, target_column):
    """Implements a simple linear regression model for forecasting."""
    X = df.drop(columns=[target_column])  # Features
    y = df[target_column]  # Target variable
    
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Create and train the model
    model = LinearRegression()
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    mse = mean_squared_error(y_test, y_pred)
    print(f"Mean Squared Error: {mse}")
    
    return model, y_test, y_pred

# 5. Visualizing Data Trends
def plot_forecast(y_test, y_pred):
    """Plots actual vs predicted values for forecasting visualization."""
    plt.figure(figsize=(10, 5))
    plt.plot(y_test.values, label="Actual Values", marker='o')
    plt.plot(y_pred, label="Predicted Values", linestyle='dashed', marker='x')
    plt.legend()
    plt.title("Actual vs Predicted Forecast")
    plt.xlabel("Data Points")
    plt.ylabel("Values")
    plt.show()

# Example Usage (Uncomment to run)
# model = create_simple_nn(input_shape=10)
# model.summary()

# sample_data = np.random.rand(100, 5)  # 100 samples, 5 features
# pca_result, variance = perform_pca(sample_data, n_components=2)
# print("PCA Variance Ratio:", variance)

# df = load_and_analyze_data("sample_data.csv")
# trained_model, actual, predicted = linear_regression_forecasting(df, target_column="Price")
# plot_forecast(actual, predicted)


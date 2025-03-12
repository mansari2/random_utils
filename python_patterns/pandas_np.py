import numpy as np
import pandas as pd

"""
This script provides common Data Science operations using NumPy and Pandas.

NumPy Operations:
- Creating and manipulating arrays
- Basic mathematical operations
- Aggregation functions
- Reshaping and filtering data

Pandas Operations:
- Creating and manipulating DataFrames
- Handling missing data
- Grouping and aggregations
- Merging and joining datasets
"""

# 1. NumPy Operations

def numpy_operations():
    # Creating an array
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print("NumPy Array:\n", arr)
    
    # Basic operations
    print("Sum of all elements:", np.sum(arr))
    print("Mean:", np.mean(arr))
    print("Standard Deviation:", np.std(arr))
    
    # Reshaping
    reshaped = arr.reshape(3, 2)
    print("Reshaped Array:\n", reshaped)
    
    # Filtering
    print("Elements greater than 3:", arr[arr > 3])

# 2. Pandas Operations

def pandas_operations():
    # Creating a DataFrame
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35], 'Score': [85, 90, 95]}
    df = pd.DataFrame(data)
    print("Pandas DataFrame:\n", df)
    
    # Handling missing data
    df.loc[1, 'Score'] = np.nan  # Introduce NaN
    print("\nDataFrame with NaN:\n", df)
    df.fillna(df['Score'].mean(), inplace=True)  # Fill NaN with mean
    print("\nAfter filling NaN:\n", df)
    
    # Grouping and aggregations
    grouped = df.groupby('Age').mean()
    print("\nGrouped by Age:\n", grouped)
    
    # Merging DataFrames
    extra_data = pd.DataFrame({'Name': ['Alice', 'Charlie'], 'City': ['NY', 'LA']})
    merged_df = df.merge(extra_data, on='Name', how='left')
    print("\nMerged DataFrame:\n", merged_df)

# Example usage (Uncomment to run)
# numpy_operations()
# pandas_operations()


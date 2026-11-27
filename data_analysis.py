import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# Generate a sample dataset
np.random.seed(42)
data = {
    "age": np.random.randint(20, 60, 100),
    "salary": np.random.randint(22000, 85000, 100),
    "experience": np.random.randint(0, 25, 100),
    "department": np.random.choice(["IT", "HR", "Sales"], 100)
}

df = pd.DataFrame(data)

# Explore the dataset
print("Dataset overview:")
print(df.describe())
print("\nMissing values:")
print(df.isnull().sum())

# Calculate department statistics
department_stats = df.groupby("department").agg(
    avg_salary=("salary", "mean"),
    avg_experience=("experience", "mean"),
    employee_count=("age", "count")
)

print("\nDepartment statistics:")
print(department_stats)
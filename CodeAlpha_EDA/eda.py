# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Titanic_Dataset.csv")

# Show first rows
print(df.head())

# Dataset information
print(df.info())

# Missing values
print(df.isnull().sum())

# Survival count plot
sns.countplot(x="Survived", data=df)

# Chart title
plt.title("Survival Count")

# Save chart
plt.savefig("survival_chart.png")

# Show chart
plt.show()

# Average age
print("Average Age:", df["Age"].mean())

# Gender count
print(df["Sex"].value_counts())
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
print(os.getcwd())

# CSV file load
df = pd.read_csv("Titanic.csv")

print("===== FIRST 5 ROWS =====")
print(df.head())

# Dataset Information

print("\n===== DATASET INFO =====")
print(df.info())

print("\n===== DATASET SHAPE =====")
print(df.shape)

print("\n===== COLUMN NAMES =====")
print(df.columns)

# Check Missing Values

print("\n===== MISSING VALUES =====")
print(df.isnull().sum())

# Fill Missing Age Values

df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill Embarked Missing Values
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

print("\n===== AFTER HANDLING MISSING VALUES =====")
print(df.isnull().sum())

# Survival Count

survival_count = df["Survived"].value_counts()

print("\n===== SURVIVAL COUNT =====")
print(survival_count)

# Survival Bar Chart

plt.bar(["Not Survived", "Survived"],
        survival_count,
        color=["red", "green"])

plt.title("Titanic Survival Count")
plt.xlabel("Status")
plt.ylabel("Number of Passengers")

plt.show()

# Gender Count

gender_count = df["Sex"].value_counts()

print("\n===== GENDER COUNT =====")
print(gender_count)

#  Gender Pie Chart

plt.pie(gender_count,
        labels=gender_count.index,
        autopct='%1.1f%%')

plt.title("Male vs Female Passengers")

plt.show()

#  Passenger Class Count

pclass_count = df["Pclass"].value_counts()

print("\n===== PASSENGER CLASS COUNT =====")
print(pclass_count)

# Passenger Class Bar Chart

plt.bar(pclass_count.index,
        pclass_count.values,
        color=["blue", "orange", "purple"])

plt.title("Passenger Class Distribution")
plt.xlabel("Passenger Class")
plt.ylabel("Count")

plt.show()

# Age Distribution Histogram

plt.hist(df["Age"], bins=10)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.show()

# EXTRA PLOT 1 : Fare Distribution

plt.hist(df["Fare"], bins=15)

plt.title("Fare Distribution")
plt.xlabel("Fare")
plt.ylabel("Frequency")

plt.show()

# EXTRA PLOT 2 : Survival by Gender

survival_gender = pd.crosstab(df["Sex"], df["Survived"])

print("\n===== SURVIVAL BY GENDER =====")
print(survival_gender)

survival_gender.plot(kind="bar")

plt.title("Survival Based on Gender")
plt.xlabel("Gender")
plt.ylabel("Count")

plt.show()

# EXTRA PLOT 3 : Survival by Passenger Class

survival_class = pd.crosstab(df["Pclass"], df["Survived"])

print("\n===== SURVIVAL BY PASSENGER CLASS =====")
print(survival_class)

survival_class.plot(kind="bar")

plt.title("Survival Based on Passenger Class")
plt.xlabel("Passenger Class")
plt.ylabel("Count")

plt.show()

#  Correlation Matrix

numeric_df = df.select_dtypes(include=np.number)

correlation = numeric_df.corr()

print("\n===== CORRELATION MATRIX =====")
print(correlation)

print("\nTitanic EDA Completed Successfully!")
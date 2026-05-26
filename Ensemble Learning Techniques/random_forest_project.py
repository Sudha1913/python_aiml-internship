# =====================================================
# ENSEMBLE LEARNING TECHNIQUES PROJECT
# DATASET: NETFLIX TITLES DATASET
# BAGGING - BOOSTING - STACKING
# =====================================================

# =========================
# IMPORT LIBRARIES
# =========================

import pandas as pd
import matplotlib.pyplot as plt
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

# Ensemble Algorithms
from sklearn.ensemble import (
    RandomForestClassifier,
    AdaBoostClassifier,
    StackingClassifier
)

# Other Algorithms
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier

# Metrics
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

# =====================================================
# LOAD DATASET
# =====================================================

df = pd.read_csv("netflix_titles.csv")

# =====================================================
# DISPLAY DATASET
# =====================================================

print("FIRST 5 ROWS")
print(df.head())

print("\nDATASET SHAPE")
print(df.shape)

print("\nMISSING VALUES")
print(df.isnull().sum())

# =====================================================
# SELECT IMPORTANT COLUMNS
# =====================================================

df = df[[
    "type",
    "release_year",
    "rating",
    "country"
]]

# =====================================================
# REMOVE MISSING VALUES
# =====================================================

df = df.dropna()

# =====================================================
# REMOVE DUPLICATES
# =====================================================

df = df.drop_duplicates()

# =====================================================
# ENCODE CATEGORICAL COLUMNS
# =====================================================

le_type = LabelEncoder()
le_rating = LabelEncoder()
le_country = LabelEncoder()

df["type"] = le_type.fit_transform(df["type"])

df["rating"] = le_rating.fit_transform(df["rating"])

df["country"] = le_country.fit_transform(df["country"])

# =====================================================
# FEATURES AND TARGET
# =====================================================

X = df[[
    "release_year",
    "rating",
    "country"
]]

y = df["type"]

# =====================================================
# TRAIN TEST SPLIT
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

print("\nTRAIN DATA SHAPE:", X_train.shape)

print("TEST DATA SHAPE:", X_test.shape)

# =====================================================
# 1. BAGGING - RANDOM FOREST
# =====================================================

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

rf_accuracy = accuracy_score(y_test, rf_pred)

print("\nRANDOM FOREST ACCURACY")
print(rf_accuracy)

# =====================================================
# 2. BOOSTING - ADABOOST
# =====================================================

ab_model = AdaBoostClassifier(
    n_estimators=100,
    random_state=42
)

ab_model.fit(X_train, y_train)

ab_pred = ab_model.predict(X_test)

ab_accuracy = accuracy_score(y_test, ab_pred)

print("\nADABOOST ACCURACY")
print(ab_accuracy)

# =====================================================
# 3. STACKING
# =====================================================

estimators = [
    ("dt", DecisionTreeClassifier()),
    ("lr", LogisticRegression())
]

stack_model = StackingClassifier(
    estimators=estimators,
    final_estimator=LogisticRegression()
)

stack_model.fit(X_train, y_train)

stack_pred = stack_model.predict(X_test)

stack_accuracy = accuracy_score(
    y_test,
    stack_pred
)

print("\nSTACKING ACCURACY")
print(stack_accuracy)

# =====================================================
# RANDOM FOREST CLASSIFICATION REPORT
# =====================================================

print("\nRANDOM FOREST CLASSIFICATION REPORT")

print(
    classification_report(
        y_test,
        rf_pred,
        target_names=["Movie", "TV Show"]
    )
)

# =====================================================
# CONFUSION MATRIX
# =====================================================

cm = confusion_matrix(y_test, rf_pred)

disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Movie", "TV Show"]
)

disp.plot(cmap="Blues")

plt.title("Random Forest Confusion Matrix")

plt.show()

# =====================================================
# ACCURACY COMPARISON CHART
# =====================================================

models = [
    "Random Forest",
    "AdaBoost",
    "Stacking"
]

accuracies = [
    rf_accuracy,
    ab_accuracy,
    stack_accuracy
]

plt.figure(figsize=(8,5))

plt.bar(models, accuracies)

plt.xlabel("Algorithms")

plt.ylabel("Accuracy")

plt.title("Ensemble Learning Accuracy Comparison")

plt.show()

# =====================================================
# PREDICTED TABLE
# =====================================================

predicted_table = X_test.copy()

predicted_table["Actual_Type"] = y_test.values

predicted_table["Predicted_Type"] = rf_pred

# Convert numeric labels back to original text
predicted_table["Actual_Type"] = le_type.inverse_transform(
    predicted_table["Actual_Type"]
)

predicted_table["Predicted_Type"] = le_type.inverse_transform(
    predicted_table["Predicted_Type"]
)

print("\nPREDICTED TABLE")

print(predicted_table.head(20))

# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(
    rf_model,
    "random_forest_model.pkl"
)

print("\nMODEL SAVED SUCCESSFULLY!")

# =====================================================
# EXTERNAL PREDICTION
# =====================================================

# Example:
# release_year = 2020
# rating = TV-MA
# country = India

new_data = [[
    2020,
    le_rating.transform(["TV-MA"])[0],
    le_country.transform(["India"])[0]
]]

new_df = pd.DataFrame(
    new_data,
    columns=X.columns
)

result = rf_model.predict(new_df)[0]

print("\nEXTERNAL PREDICTION")

print(
    "Predicted Type:",
    le_type.inverse_transform([result])[0]
)

# ============================================================
# Customer Churn Analysis - Step 1: Data Cleaning
# ============================================================

import pandas as pd
import numpy as np

# ---------- 1. LOAD DATA ----------
print("=" * 50)
print("1. Loading data...")
print("=" * 50)

df = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')

print(f"Data loaded! Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print("\nFirst 5 rows:")
print(df.head())


# ---------- 2. INITIAL DATA INFO ----------
print("\n" + "=" * 50)
print("2. Dataset Info")
print("=" * 50)
print(df.info())


# ---------- 3. CHECK MISSING VALUES ----------
print("\n" + "=" * 50)
print("3. Checking missing values...")
print("=" * 50)
print(df.isnull().sum())


# ---------- 4. FIX TOTALCHARGES COLUMN ----------
print("\n" + "=" * 50)
print("4. Fixing TotalCharges column...")
print("=" * 50)

# Step 4.1: Check current data type
print(f"Data type before: {df['TotalCharges'].dtype}")

# Step 4.2: Convert to numeric
# errors='coerce' will turn invalid entries into NaN
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

missing_count = df['TotalCharges'].isnull().sum()
print(f" Converted to numeric! New data type: {df['TotalCharges'].dtype}")
print(f" Missing values found: {missing_count}")

# Step 4.3: Look at those rows (who are they?)
print("\nRows with missing TotalCharges (check tenure — all should be 0):")
print(df[df['TotalCharges'].isnull()][['tenure', 'MonthlyCharges', 'TotalCharges', 'Churn']])

# Step 4.4: Fill missing values with 0 (new customers — no bill yet)
df['TotalCharges'] = df['TotalCharges'].fillna(0)
print(f" Filled missing values with 0! Now missing values: {df['TotalCharges'].isnull().sum()}")


# ---------- 5. DROP CUSTOMER ID ----------
print("\n" + "=" * 50)
print("5. Dropping customerID column...")
print("=" * 50)

df = df.drop('customerID', axis=1)
print(f" Dropped! Now Columns: {df.shape[1]}")


# ---------- 6. FINAL CHECK ----------
print("\n" + "=" * 50)
print("6. Final check...")
print("=" * 50)

print(f" Rows: {df.shape[0]}")
print(f" Columns: {df.shape[1]}")
print(f" Total missing values: {df.isnull().sum().sum()}")
print(f" Duplicates: {df.duplicated().sum()}")
print(f" Churn count:")
print(df['Churn'].value_counts())


# ---------- 7. SAVE CLEAN DATA ----------
print("\n" + "=" * 50)
print("7. Saving cleaned data...")
print("=" * 50)

df.to_csv('telco_churn_cleaned.csv', index=False)
print(" SAVED: telco_churn_cleaned.csv")

print("\n" + "=" * 50)
print("DATA CLEANING COMPLETE! Next step: EDA (Analysis)")
print("=" * 50)
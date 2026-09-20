# ============================================================
# Customer Churn Analysis - Step 2: EDA (Analysis with Graphs)
# ============================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Style for graphs
sns.set_style('whitegrid')
plt.rcParams['figure.figsize'] = (10, 5)

# ---------- 1. LOAD CLEANED DATA ----------
print("=" * 50)
print("1. Loading cleaned data...")
print("=" * 50)

df = pd.read_csv('telco_churn_cleaned.csv')
print(f"✅ Loaded! Rows: {df.shape[0]}, Columns: {df.shape[1]}")


# ---------- 2. CHURN DISTRIBUTION ----------
print("\n" + "=" * 50)
print("2. How many customers left? (Churn Distribution)")
print("=" * 50)
print(df['Churn'].value_counts())
print(df['Churn'].value_counts(normalize=True) * 100)

fig, ax = plt.subplots(1, 2, figsize=(12, 5))

# Count plot
sns.countplot(x='Churn', data=df, ax=ax[0], palette=['#2ecc71', '#e74c3c'])
ax[0].set_title('Churn Count', fontsize=14, fontweight='bold')

# Pie chart
df['Churn'].value_counts().plot.pie(autopct='%1.1f%%', ax=ax[1], 
                                     colors=['#2ecc71', '#e74c3c'], explode=[0, 0.1])
ax[1].set_title('Churn Percentage', fontsize=14, fontweight='bold')

plt.tight_layout()
plt.savefig('1_churn_distribution.png', dpi=100)
plt.show()
print("✅ Saved: 1_churn_distribution.png")


# ---------- 3. CHURN BY CONTRACT TYPE ----------
print("\n" + "=" * 50)
print("3. Churn by Contract Type (Key Insight!)")
print("=" * 50)
print(pd.crosstab(df['Contract'], df['Churn'], margins=True))

plt.figure(figsize=(10, 5))
sns.countplot(x='Contract', hue='Churn', data=df, palette=['#2ecc71', '#e74c3c'])
plt.title('Churn by Contract Type', fontsize=14, fontweight='bold')
plt.xlabel('Contract Type')
plt.ylabel('Number of Customers')
plt.legend(title='Churn')
plt.tight_layout()
plt.savefig('2_churn_by_contract.png', dpi=100)
plt.show()
print("✅ Saved: 2_churn_by_contract.png")


# ---------- 4. CHURN BY TENURE ----------
print("\n" + "=" * 50)
print("4. Churn by Tenure (How long customers stayed)")
print("=" * 50)

plt.figure(figsize=(12, 5))
sns.histplot(data=df, x='tenure', hue='Churn', bins=30, 
             palette=['#2ecc71', '#e74c3c'], multiple='stack')
plt.title('Churn by Tenure (Months)', fontsize=14, fontweight='bold')
plt.xlabel('Tenure (Months)')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig('3_churn_by_tenure.png', dpi=100)
plt.show()
print("✅ Saved: 3_churn_by_tenure.png")

print("\nAverage tenure:")
print(df.groupby('Churn')['tenure'].mean())


# ---------- 5. CHURN BY MONTHLY CHARGES ----------
print("\n" + "=" * 50)
print("5. Churn by Monthly Charges")
print("=" * 50)

plt.figure(figsize=(12, 5))
sns.kdeplot(data=df, x='MonthlyCharges', hue='Churn', fill=True, 
            palette=['#2ecc71', '#e74c3c'])
plt.title('Churn by Monthly Charges', fontsize=14, fontweight='bold')
plt.xlabel('Monthly Charges')
plt.ylabel('Density')
plt.tight_layout()
plt.savefig('4_churn_by_monthly_charges.png', dpi=100)
plt.show()
print("✅ Saved: 4_churn_by_monthly_charges.png")

print("\nAverage Monthly Charges:")
print(df.groupby('Churn')['MonthlyCharges'].mean())


# ---------- 6. CHURN BY INTERNET SERVICE ----------
print("\n" + "=" * 50)
print("6. Churn by Internet Service Type")
print("=" * 50)
print(pd.crosstab(df['InternetService'], df['Churn'], margins=True))

plt.figure(figsize=(10, 5))
sns.countplot(x='InternetService', hue='Churn', data=df, 
              palette=['#2ecc71', '#e74c3c'])
plt.title('Churn by Internet Service', fontsize=14, fontweight='bold')
plt.xlabel('Internet Service Type')
plt.ylabel('Number of Customers')
plt.tight_layout()
plt.savefig('5_churn_by_internet.png', dpi=100)
plt.show()
print("✅ Saved: 5_churn_by_internet.png")


# ---------- 7. CHURN BY PAYMENT METHOD ----------
print("\n" + "=" * 50)
print("7. Churn by Payment Method")
print("=" * 50)

plt.figure(figsize=(12, 5))
sns.countplot(x='PaymentMethod', hue='Churn', data=df, 
              palette=['#2ecc71', '#e74c3c'])
plt.title('Churn by Payment Method', fontsize=14, fontweight='bold')
plt.xlabel('Payment Method')
plt.ylabel('Number of Customers')
plt.xticks(rotation=15)
plt.tight_layout()
plt.savefig('6_churn_by_payment.png', dpi=100)
plt.show()
print("✅ Saved: 6_churn_by_payment.png")


# ---------- 8. SUMMARY OF INSIGHTS ----------
print("\n" + "=" * 50)
print("🎉 EDA COMPLETE! KEY INSIGHTS:")
print("=" * 50)
print("""

📌 1. 26.5% of customers have churned (left the company)

📌 2. Month-to-month contracts have MUCH higher churn 
      than One/Two year contracts

📌 3. New customers (low tenure) churn the most —
      customers who stay past the first few months tend to stay long

📌 4. Customers with higher Monthly Charges churn more

📌 5. Fiber optic users churn MORE than DSL users

📌 6. Electronic check users churn the most —
      automatic payments (bank/credit card) churn the least

✅ All graphs saved as PNG files in your folder!
""")
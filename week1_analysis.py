import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# --- STEP 1: LOAD DATA ---
print("Loading dataset...")
try:
    df = pd.read_csv('dataset_phishing.csv')
   
except FileNotFoundError:
    print("❌ Error: 'dataset_phishing.csv' not found. Make sure it is in the same folder.")
    exit()

# --- STEP 2: GET NUMBERS FOR YOUR REPORT ---
print(f"1. Total Rows (Websites): {df.shape[0]}")
print(f"2. Total Columns (Features): {df.shape[1]}")

# Check for missing values
missing = df.isnull().sum().sum()
print(f"3. Missing Values: {missing}")

# Check Class Distribution (Phishing vs Legitimate)
# In your file, the target column is named 'status'
print(df['status'].value_counts())

# --- STEP 3: GENERATE CHARTS (Popups will appear) ---
print("\n--- GENERATING CHARTS... (Close each popup to see the next one) ---")

# Chart 1: Bar Plot of Phishing vs Legitimate
plt.figure(figsize=(6, 4))
sns.countplot(x='status', data=df, palette='viridis')
plt.title('Distribution: Phishing vs Legitimate')
plt.xlabel('Website Status')
plt.ylabel('Count')
plt.tight_layout()
plt.show()

# Chart 2: Correlation Heatmap (Selected Features)
# We pick numerical columns to see relationships
features = ['length_url', 'nb_dots', 'nb_hyphens', 'ratio_digits_url']
plt.figure(figsize=(8, 6))
sns.heatmap(df[features].corr(), annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap of Key Features')
plt.tight_layout()
plt.show()

# Chart 3: URL Length Comparison
plt.figure(figsize=(8, 5))
sns.boxplot(x='status', y='length_url', data=df, showfliers=False)
plt.title('URL Length: Phishing vs Legitimate')
plt.show()

print("\n✅ Analysis Complete! Use these charts for your Week 1 Deliverable.")